import numpy as np

from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import auc, roc_auc_score, precision_recall_curve
from sklearn.utils import deprecated


def __adjust_predictions(score: np.ndarray, label: np.ndarray, delay=None, inplace=False) -> np.ndarray:
    assert np.shape(score) == np.shape(label)
    if delay is None:
        delay = len(score)
    splits = np.where(label[1:] != label[:-1])[0] + 1
    is_anomaly = label[0] == 1
    new_array = np.copy(score) if not inplace else score
    pos = 0
    for sp in splits:
        if is_anomaly:
            ptr = min(pos + delay + 1, sp)
            new_array[pos: ptr] = np.max(new_array[pos: ptr])
            new_array[ptr: sp] = np.maximum(new_array[ptr: sp], new_array[pos])
        is_anomaly = not is_anomaly
        pos = sp
    sp = len(label)
    if is_anomaly:
        ptr = min(pos + delay + 1, sp)
        new_array[pos: sp] = np.max(new_array[pos: ptr])
    return new_array


def __ignore_missing(*args, missing):
    result = []
    for arr in args:
        _arr = np.copy(arr)
        result.append(_arr[missing != 1])
    return tuple(result)


@deprecated('Using precision to evaluate anomaly detection algorithms is not recommended.')
def best_precision(score: np.ndarray, label: np.ndarray, delay: int=None):
    if delay is not None:
        score = __adjust_predictions(score, label, delay=delay, inplace=False)

    ps, rs, ts = precision_recall_curve(label, score)
    fs = 2 * ps * rs / np.clip(ps + rs, a_min=1e-8, a_max=None)

    return ps[np.argmax(fs)]


@deprecated('Using recall to evaluate anomaly detection algorithms is not recommended.')
def best_recall(score: np.ndarray, label: np.ndarray, delay: int=None):
    if delay is not None:
        score = __adjust_predictions(score, label, delay=delay, inplace=False)

    ps, rs, ts = precision_recall_curve(label, score)
    fs = 2 * ps * rs / np.clip(ps + rs, a_min=1e-8, a_max=None)

    return rs[np.argmax(fs)]


@deprecated('Using F1-score to evaluate anomaly detection algorithms is not recommended.')
def best_f1(score: np.ndarray, label: np.ndarray, delay: int=None):
    if delay is not None:
        score = __adjust_predictions(score, label, delay=delay, inplace=False)

    ps, rs, ts = precision_recall_curve(label, score)
    fs = 2 * ps * rs / np.clip(ps + rs, a_min=1e-8, a_max=None)

    return np.max(fs[np.isfinite((fs))])


def roc_auc(score: np.ndarray, label: np.ndarray, delay: int=None):
    if delay is not None:
        score = __adjust_predictions(score, label, delay=delay, inplace=False)

    return roc_auc_score(label, score)


def pr_auc(score: np.ndarray, label: np.ndarray, delay: int=None):
    if delay is not None:
        score = __adjust_predictions(score, label, delay=delay, inplace=False)

    ps, rs, _ = precision_recall_curve(label, score)
    ids = np.argsort(rs)

    return auc(rs[ids], ps[ids])
