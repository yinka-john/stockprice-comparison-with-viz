#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine


# In[2]:


engine = create_engine("sqlite:///Stockpricedata.db")


# In[3]:


#getting financial info from microsoft
obj = yf.Ticker("MSFT")


# In[4]:


#getting table of stocks of varoius companies from wikipedia
dow= pd.read_html("https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average")


# In[5]:


dow


# In[6]:


#subsetting the table for companies and their details
dow[1]
#storing the symbols column on the above table in a list
symbols = dow[1].Symbol.to_list()


# In[7]:


symbols


# In[8]:


infos = []

for symbol in symbols:
    inf = yf.Ticker(symbol).info
    infos.append(inf)


# In[9]:


infos


# In[10]:


df = pd.DataFrame(infos)


# In[12]:


df = df.drop(columns="companyOfficers")


# In[13]:


df.to_sql("Fundamental_data", engine, index=False)


# In[15]:


pd.read_sql("Fundamental_data", engine)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




