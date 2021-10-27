"""
@Time    : 2021/10/24 11:23
@File    : detectors.py
@Software: PyCharm
@Desc    : 
"""
import abc
from typing import Union, IO

import numpy as np

from pyadts.utils.io import save_objects, load_objects
from .data import TimeSeriesRepository


class Detector(abc.ABC):
    def __int__(self):
        pass

    @abc.abstractmethod
    def fit(self, x: Union[np.ndarray, TimeSeriesRepository], y: np.ndarray = None):
        pass

    @abc.abstractmethod
    def predict(self, x: Union[np.ndarray, TimeSeriesRepository]):
        pass

    @abc.abstractmethod
    def score(self, x: Union[np.ndarray, TimeSeriesRepository]):
        pass

    # @abc.abstractmethod
    def save(self, f: Union[str, IO]):
        print(self.__dict__)
        save_objects(self.__dict__, f)

    # @abc.abstractmethod
    def load(self, f: Union[str, IO]):
        objs = load_objects(f)
        print(objs)
        self.__dict__.update(objs)
