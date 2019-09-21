#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Extract stock prices. every day, five day a week@ 4pm


# In[5]:

from crontab import CronTab
cron = CronTab(tab="""*/5 * * * * /usr/local/bin/python3 /Users/bharats/personal/workspace/python/market/extractor.py""")
cron.write()

for job in cron:
    print(job.is_valid())

