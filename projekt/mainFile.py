__author__ = 'wemstar'

from projekt.Enums import OptionType,BarierType
from projekt.PriceFunction import normalOption,BarierOprionModel
from projekt.BinomialImplementation import binomial





barierTzpe=BarierOprionModel(OptionType.Call,180.0,BarierType.Out)
print(binomial(S0=98.0, T=1., r=0.05, vola=0.2, M=1000, strike=100.0,function=barierTzpe))
