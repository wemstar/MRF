__author__ = 'wemstar'
import numpy as np
from projekt.Enums import OptionType, BarierType


def normalOptionCall(S, strike):
    return np.maximum(S - strike, 0)
def normalOptionPut(S, strike):
    return np.maximum(strike-S, 0)


class BarierOprionModel:
    def __init__(self, optionType, barierPrice, barierType):
        self.optionType = optionType
        self.barierPrice = barierPrice
        self.barierType = barierType

    def __call__(self, S0, strike):
        result = []
        if self.optionType == OptionType.Put:
            result = np.maximum(strike - S0, 0.)
        else:
            result = np.maximum(S0 - strike, 0.)

        if self.barierType == BarierType.In:
            result[(S0 -  self.barierPrice) < 0.] = 0.
        else:
            result[(self.barierPrice  - S0) < 0.] = 0.
        return result


