
# coding: utf-8

# In[2]:


#TOC39EXERCISE4_QUESTION1
def do_twice(f):
    f()
    f()
    
def print_spam():
    print ("spam")

#TOC39EXERCISE4_QUESTION2
def do_twice(f,a):
    f(a)
    f(a)

#TOC39EXERCISE4_QUESTION3
def print_twice(a):
    print (a)
    print (a)
#TOC39EXERCISE4_QUESTION4
do_twice(print_twice,"spam")
#TOC39EXERCISE4_QUESTION5
def do_four(g,b):
    do_twice(g,b)
    do_twice(g,b)
    
do_four(print_twice,'pepsi')

