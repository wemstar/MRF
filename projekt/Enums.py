__author__ = 'wemstar'
from enum import Enum

class BarierType(Enum):
    In = 1
    Out = 2

class OptionType(Enum):
    Put = 1
    Call = 2