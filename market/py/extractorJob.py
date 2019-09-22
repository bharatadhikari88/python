#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Extract stock prices. every day, five day a week@ 4pm

import os
import schedule
import time
from Extractor import Extractor

def runExtractor():
    Extractor().extract()

schedule.every().monday.at("16:00").do(runExtractor)
schedule.every().tuesday.at("16:00").do(runExtractor)
schedule.every().wednesday.at("16:00").do(runExtractor)
schedule.every().thursday.at("16:00").do(runExtractor)
schedule.every().friday.at("16:00").do(runExtractor)

if __name__== "__main__":
    while True:
        print("Once in a hour look for pending jobs")
        schedule.run_pending()
        time.sleep(60*60) ## every hour

