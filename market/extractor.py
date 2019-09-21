#!/usr/bin/env python
# coding: utf-8

# In[144]:


from nsetools import Nse
import pandas as pd
import numpy as np

nse = Nse()


# ### stock name to code mapping

# In[145]:


stockCodes = nse.get_stock_codes()
if stockCodes.get('SYMBOL'):
    del stockCodes['SYMBOL'] 
stockNameKey = dict(map(reversed,stockCodes.items()))
stockNames = list(stockNameKey.keys())
stockNames


# ### stock name for lookup

# In[161]:


stocks = list(pd.read_csv("stock_lookup.csv")["Stock Names or Symbol"])
validStocks = []

for stock in stocks:
    if nse.is_valid_code(stock):
        validStocks.append(stock)
    else:
        found = False
        for stockName in stockNames:
            if stockName.find(stock) > -1:
                validStocks.append(stockNameKey.get(stockName))
                found = True
                break
        if not found:
            print("{} is invalid.".format(stock))
                
validStocks


# ### Fetch nse data for valid stocks of current date

# In[189]:


from pandas import DataFrame
from os import path
import nsepy as nsepy
import datetime as dt
from urllib.parse import quote

BASE_FOLDER = "stocks/"

def writeToCsv(stock):
    filePath = BASE_FOLDER + stock + ".csv"
    
    record = nsepy.get_quote(quote(stock))
    
    df = DataFrame(data=[[dt.datetime.now().date(),record['previousClose'],record['open'],record['dayHigh'],record['dayLow'],record['lastPrice']]],
                   columns=['Date','PClose','Open','High','Low','Close'])

    #df.reset_index(level=0, inplace=True)

    if path.exists(filePath):
        df.to_csv(filePath,mode='a',index=False, header=False)
    else:
        df.to_csv(filePath,index=False)
        
        
list(map(writeToCsv,validStocks))

    


# ### fetch historical data (one time process)
