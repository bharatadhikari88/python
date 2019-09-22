#!/usr/bin/env python
# coding: utf-8

# In[60]:


from Extractor import Extractor
import nsepy as nsepy
import datetime as dt
from pandas import DataFrame
from os import path
from urllib.parse import quote
import sys


# In[92]:

class HistoricData:
    extractor = Extractor()
    startDate = dt.date.today()
    endDate = dt.date.today()
    
    def __init__(self,startDate=None,endDate=None):
        if startDate is not None:
            self.startDate = dt.datetime.strptime(startDate,"%Y-%m-%d")
        if endDate is not None:
            self.endDate = dt.datetime.strptime(endDate,"%Y-%m-%d")
    
    
    def writeToCsv(self,stock):
        filePath = self.extractor.BASE_FOLDER + stock + ".csv"

        record = nsepy.get_history(symbol=quote(stock), start=self.startDate, end=self.endDate)
        record.reset_index(level=0, inplace=True)
        record["PClose"] = record["Prev Close"]

        df = DataFrame(record,columns=['Date','PClose','Open','High','Low','Close'])

        if path.exists(filePath):
            df.to_csv(filePath,mode='a',index=False, header=False)
        else:
            df.to_csv(filePath,index=False)
            
      
    def extractHistoricData(self):
        list(map(self.writeToCsv,self.extractor.getValidStockNames()))
        
        
# In[95]:

if __name__== "__main__":
    if len(sys.argv) == 3:
        HistoricData(sys.argv[1],sys.argv[2]).extractHistoricData()
    else:
        HistoricData(input("Start date(eg: 2019-11-31) "),input("End date(eg: 2019-11-31) ")).extractHistoricData()


