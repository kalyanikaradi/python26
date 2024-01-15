#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import pandas as np


# In[3]:


#slicing
d= pd.Series([1,2,3,44,56,789,655,32,12])
d


# In[4]:


d[0:3]


# In[6]:


d[3:8]


# In[8]:


d[[3,4,8,2,5]]


# In[9]:


#replace
d[3:5]=[567,221]
d


# In[12]:


arr3=np.array([2,3,4,5])
s1=pd.Series(arr3)
s1


# In[14]:


print(s1)


# In[15]:


arr4=np.array([1,2,3,4])
s=pd.Series(arr4,index=['one','two','three','four'])
s


# In[16]:


print(s)


# In[ ]:




