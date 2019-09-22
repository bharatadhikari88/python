#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Extract stock prices. every day, five day a week@ 4pm


# In[1]:

from crontab import CronTab

if __name__== "__main__":
	cron = CronTab(tab="""*/1 *  * * 0-5 python3 Extractor.py""")
	cron.write()