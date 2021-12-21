from pandas_datareader import data
from matplotlib import pyplot as plt

#df = data.DataReader('NIKKEI225', 'fred')
df = data.DataReader('^N225', 'yahoo')
plt.plot(df)
plt.show()
