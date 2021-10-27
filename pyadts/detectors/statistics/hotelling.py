"""
@Time    : 2021/10/26 0:17
@File    : hotelling.py
@Software: PyCharm
@Desc    : 
"""
from typing import Union

import numpy as np

from pyadts.generic import Detector, TimeSeriesRepository


class HotellingDetector(Detector):
    def __init__(self):
        super(HotellingDetector, self).__init__()

    def fit(self, x: Union[np.ndarray, TimeSeriesRepository], y: np.ndarray = None):
        pass

    def predict(self, x: Union[np.ndarray, TimeSeriesRepository]):
        pass

    def score(self, x: Union[np.ndarray, TimeSeriesRepository]):
        pass
