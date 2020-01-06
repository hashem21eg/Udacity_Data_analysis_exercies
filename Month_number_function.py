#!/usr/bin/env python
# coding: utf-8

# In[1]:


def how_many_days(month_number):
    month_list = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    month_name = [0,'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    return "Month name is {}".format(month_name[month_number]), "number of Days is {}".format(month_list[month_number])


# In[2]:


how_many_days(8)


# In[ ]:




