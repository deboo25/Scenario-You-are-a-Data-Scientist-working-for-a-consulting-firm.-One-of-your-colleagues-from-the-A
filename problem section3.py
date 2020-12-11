#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as np


# In[4]:


revenue=np.array([14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09,

10305.32, 14379.96, 10713.97, 15433.50])


# In[5]:


expenses=np.array([12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12,

6976.93, 16618.61, 10054.37, 3803.96])


# In[32]:


#profit 
a=range(0,12)
A=[0,0,0,0,0,0,0,0,0,0,0,0]


# In[34]:


for i in a :
    t=revenue[i]-expenses[i]
    A[i]=t
A


# In[10]:


#ptofit after tax


# In[39]:


X=[0,0,0,0,0,0,0,0,0,0,0,0]
for i in a:
    t=A[i]*0.3
    X[i]=t
X


# In[17]:


#profit margin


# In[40]:


Y=[0,0,0,0,0,0,0,0,0,0,0,0]
for i in a:
    t1=X[i]/revenue[i]
    Y[i]=t1
Y


# In[48]:


g=revenue.mean()
g


# In[49]:


# good months


# In[50]:


M=[0,0,0,0,0,0,0,0,0,0,0,0]
for i in a:
    if X[i]>g:
        M[i]=1
M


# In[ ]:




