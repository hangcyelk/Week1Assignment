
# coding: utf-8

# In[2]:


def right_justify(s):
    length = len(s)
    new_string = (70-length+1)*" "+s
    return new_string

right_justify('allen')

