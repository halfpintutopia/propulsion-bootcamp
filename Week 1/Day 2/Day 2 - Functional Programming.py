
# coding: utf-8

# In[3]:


# python treats functions as first class objects
def say_hello(name):
    print(f"Hello my name is {name}")


# In[4]:


say_hello("Simon")


# In[5]:


say = say_hello # assigning the function to a variable
say == say_hello


# In[6]:


def greeting(intro_fn, name):
    print("Hi there!")
    intro_fn(name)
    print("Nice to meet you")


# In[7]:


greeting(say_hello, "Simon")


# In[ ]:


#lambda functions
sqr_1 = lambda x: x*x # an anonymous function - without a name


# In[ ]:


mul = lambda x, y: x*y
mul(10,20)


# In[ ]:


#multip
def mult(arr):
    new_list = []
    for element in arr:
        new_list.append(element*2)
    return new_list

mult([1, 10, 100])


# In[8]:


def multiply_2(val):
    return val*2
list(map(multiply_2, [1, 10, 100])) # map good for writing small bit of code - only evaluated for however long you need it


# In[9]:


list(map(lambda x: x*2, [1, 10, 101])) 


# In[10]:


countries = ["Switzerland", "Russia", "USA", "Panama"]


# In[11]:


list(map(len, countries))


# In[12]:


[len(c) for c in countries]


# In[14]:


def times2(x): return x*2
def times3(x): return x*3

fun = [times2, times3]
#function lambda already expects a is a function
list(map(lambda a: a(10), fun))


# In[15]:


numbers = [10, 20, 30, 40, 60, 70, 80, 90]


# In[16]:


#version 1 with filter
list(filter(lambda x: x%3==0, numbers))


# In[17]:


#version 2 with filter - for more complex uses of filter define the function
def is3(x):
    return x%3==0

list(filter(is3, numbers))


# In[18]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_multiple_of_three(n):
    return n % 3 == 0


print(list(filter(is_multiple_of_three, numbers)))
# result: [3, 6, 9]


# In[24]:


numbers = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

even_numbers = list(filter(lambda num%2))
# def is_multiple_of_three(n):
#     return n % 3 == 0


print(list(filter(even_numbers, numbers)))
# result: [3, 6, 9]


# In[32]:


list(filter((lambda num: num%2==0), [1,2,3,4,5,6,7,8,9,10]))

# print(list(1,2,3,4,5,6,7,8,9,10))


# In[35]:


list(map((lambda num: num**0.5 != float), [1,2,3,4,5,6,7,8,9,10]))


# In[36]:


from math import sqrt


# In[41]:


list(map((lambda num: sqrt(num).is_integer()), [1,2,3,4,5,6,7,8,9,10]))


# In[42]:


li1 = [1,2,3,4,5,6,7,8,9,10]
print(list(filter((lambda num: num%2==0), li1)))


# In[48]:


li2 = [1,2,3,4,5,6,7,8,9,10]
list(map(filter(lambda num: sqrt(num).is_integer() or num%2==0), li2))


# In[51]:


li2 = [1,2,3,4,5,6,7,8,9,10]
print(list(map(filter((lambda num: sqrt(num).is_integer() or num%2==0), li2))))


# In[65]:


def find_numbers(min, max):
    rangeof_nums = list(range(min, max))
    div7 = []
    for i in rangeof_nums:
        if i%7 == 0 and i%5 != 0:
            div7.append(i)
    return div7
        
find_numbers(2, 40)


# In[58]:


list(range(2, 8))


# In[71]:


rangeofNums = list(find_numbers(2, 40))

print(filter(lambda num: num % 7 == 0 and num % 5 != 0), rangeofNums)
    


# In[72]:


print(filter(lambda num: num % 7 == 0 and num % 5 != 0), [0, 1, 2, 3, 4, 5, 6])

