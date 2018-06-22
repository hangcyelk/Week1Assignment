
# coding: utf-8

# In[2]:


def do_twicegrid(f):
    f()
    f()
    
def do_fourgrid(f):
    do_twicegrid(f)
    do_twicegrid(f)

def print_plusminus():
    a = '+ - - - -'
    print (a,a,'+')
    
def print_slash():
    b = '/        '
    print (b,b,'/')
    
def draw_grid():
    print_plusminus()
    do_fourgrid(print_slash)
    print_plusminus()
    do_fourgrid(print_slash)
    print_plusminus()

draw_grid()

def print_plusminus2():
    a = '+ - - - -'
    print (a,a,a,a,'+')

def print_slash2():
    b = '/        '
    print (b,b,b,b,'/')

def do_eight(f,g):
    f()
    do_fourgrid(g)
    
def draw_grid4():
    do_eight(print_plusminus2,print_slash2)
    do_eight(print_plusminus2,print_slash2)
    do_eight(print_plusminus2,print_slash2)
    do_eight(print_plusminus2,print_slash2)
    print_plusminus2()
    
draw_grid4()

