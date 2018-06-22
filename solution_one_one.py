
# coding: utf-8

# In[2]:


import math

def circle_volume():
    return 4/3*math.pi*5**3

def book_price():
    return (24.95*0.6)*60+3+59*0.75

def return_time():
    accumin = 2*8+3*7
    accusec = 2*15+3*12
    totalmin = 52+accumin+accusec/60
    finalhr = 6+math.floor(totalmin/60)
    finalmin = round(totalmin%60)
    return str(finalhr)+":"+str(finalmin)

print (circle_volume())
print (book_price())
print (return_time())

