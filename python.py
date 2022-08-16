from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import math
import numpy as np

yf.pdr_override()

samsung = pdr.get_data_yahoo('^GSPC',start='2022-07-25')
def func_max():
    return max(samsung.Close)
def func_latest():
    return samsung.Close.tail(1)

print(func_latest())


print(samsung)

print(samsung.index)
print(samsung.columns)


plt.plot(samsung.index,np.log(samsung.Close),'b',label='Samsung Electronincs')
plt.show()




