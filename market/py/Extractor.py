#!/usr/bin/env python
# coding: utf-8

# In[8]:


from nsetools import Nse
from pandas import DataFrame
from os import path
from urllib.parse import quote
import nsepy as nsepy
import datetime as dt
import pandas as pd
import numpy as np


# In[30]:


class Extractor:
    nse = Nse()
    BASE_FOLDER = "stocks/"
    LOOK_UP_FILE = "stock_lookup.csv"
    stockNameKey = {}

    def getAllStockNames(self):
        stockCodes = self.nse.get_stock_codes()
        if stockCodes.get('SYMBOL'):
            del stockCodes['SYMBOL'] 
            
        self.stockNameKey = dict(map(reversed,stockCodes.items()))
        return list(self.stockNameKey.keys())
        
    def getValidStockNames(self):
        stocks = list(pd.read_csv(self.LOOK_UP_FILE)["Stock Names or Symbol"])
        validStocks = []
        stockNames = self.getAllStockNames()

        for stock in stocks:
            if self.nse.is_valid_code(stock):
                validStocks.append(stock)
            else:
                found = False
                for stockName in stockNames:
                    if stockName.find(stock) > -1:
                        validStocks.append(self.stockNameKey.get(stockName))
                        found = True
                        break
                if not found:
                    print("{} is invalid entry in {}.".format(stock,self.LOOK_UP_FILE))
        return validStocks
    
    def writeToCsv(self,stock):
        filePath = self.BASE_FOLDER + stock + ".csv"

        record = nsepy.get_quote(quote(stock))

        df = DataFrame(data=[[dt.datetime.now().date(),record['previousClose'],record['open'],record['dayHigh'],record['dayLow'],record['lastPrice']]],
                       columns=['Date','PClose','Open','High','Low','Close'])

        #df.reset_index(level=0, inplace=True)

        if path.exists(filePath):
            df.to_csv(filePath,mode='a',index=False, header=False)
        else:
            df.to_csv(filePath,index=False)
            
    def extract(self):
        list(map(self.writeToCsv,self.getValidStockNames()))


if __name__== "__main__":
    Extractor().extract()
