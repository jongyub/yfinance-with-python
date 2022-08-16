from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import math

print("----------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")
yf.pdr_override()

snp_500 = pdr.get_data_yahoo('^GSPC',start='1984-12-5')

#print(snp_500)

#print(snp_500.index)
#print(snp_500.columns)

#plt.plot(snp_500.index,np.log10(snp_500.Close),'b',label='S&P 500')
#plt.show()

#snp_500_maximum = max(snp_500.Close)
#snp_500_today = snp_500.Close.tail(n=1)

#bear_market_indicator = (snp_500_maximum - snp_500_today ) / snp_500_maximum*100

#print(bear_market_indicator)

