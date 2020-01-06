#!/usr/bin/env python
# coding: utf-8

# In[3]:


def top_three(input_list):
    sorted_input_list = sorted(input_list, reverse = True)
    return sorted_input_list[0:3]

print(top_three([1,15,800,400,250,4332,90,70]))
    


# In[ ]:




