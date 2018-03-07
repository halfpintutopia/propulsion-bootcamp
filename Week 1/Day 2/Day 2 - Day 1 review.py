
# coding: utf-8

# In[ ]:


# loops in python 
for i in range(len(cities)):
    print()


# In[5]:


# list comprehension
[i*2 for i in range(4)]


# In[6]:


[i for i in range(4)]


# In[7]:


cars = ["BMW", "AUDI", "PORSCHE", "OPEL"]
[car for car in cars if car != "OPEL"]


# In[8]:


result = []
for car in cars:
    if car != "OPEL":
        result.append(car)


# In[9]:


[c for c in "Propulsion Academy" if c.isupper()]

# NOTE: creates a copy of the array not modifies the original array


# In[10]:


[x*2 for x in range(10) if x > 5]


# In[11]:


[x*y for x in [1,2,3] for y in [10, 100]]
# 2 for loops - 2-dimensional


# In[ ]:


# In 11 is the same as this:
result = []
for x in [1, 2, 3]:
    for y in [10, 100]:
        result.append(x*y)


# In[12]:


# Solution for Exercise 2 - Day 1
text = "Propulsion123"
[n for n in text if n.isdigit()]


# In[ ]:


# Solution for Exercise 3 - Day 1
text = "Propulsion123"
[n for n in text if n.isdigit()]


# In[13]:


def are_same_type(my_list):
    iseq = iter(my_list)
    first_type = type(next(iseq))
    # return True if all((type(x) is first_type) for x in iseq) else False
    # condenscing the code - true and false statements are redundant - as produces the same answer
    return all((type(x) is first_type) for x in iseq)

print(are_same_type(['hello', 'world', 'long sentence']))  # True


# In[ ]:


def are_same_type(my_list):
    # check we have list
    if not len(my_list):
    return True
    
    first = type(my_list[0])
    for el in my_list[1:]:
    if type(el) != first:
        return False

print(are_same_type(['hello', 'world', 'long sentence']))  # True


# In[14]:


# think of the iterator as a lens the area is still the same, just magnifies
my_list = [1, 2, 9, 10]
iseq = iter(my_list)
type(next(iseq))


# In[ ]:


# Solution for Exercise 7 - Day 1
"""
also have used a modulo %
"""


# In[16]:


def is_caught(string):
    return (int(string.find("m")) - int(string.find("C")) <= 3)

print(is_caught('C.....m'))  # False
print(is_caught('C..m'))  # True
print(is_caught('..C..m'))  # True
print(is_caught('...C...m'))  # False
print(is_caught('C.m'))  # True


# In[17]:


def zero_sum(li):
    index = len(li) - 1
    record = []
    for i in li:
        if li(i) + li(index) == 0:
            record.append(li(i), li(index))
            index = index + 1
        return record


print(zero_sum([1, 5, 0, -5, 3, -1]))  # [[0, 5], [1, 3], [2, 2]]
print(zero_sum([1, -1]))  # [[0, 1]]
print(zero_sum([0, 4, 3, 5]))  # [[0, 0]]


# In[21]:


def zero_sum(arguments):
    # go through the index
    for i in range (len(arguments)):
        print(f"i={i} arguments[i]={arguments[i]}")
            for j in range (len(arguments)):
            print(f"j={j} arguments[j]={arguments[j]}")
            
zero_sum("a", "b", "c")


# In[22]:


def zero_sum(arguments):
    # go through the index
    for i in range (len(arguments)):
        for j in range (len(arguments)):
            if arguments[i] + arguments[j] == 0:
                result.append((i,j))
        return result
        
print(zero_sum([1, 5, 0, -5, 3, -1]))    
            


# In[3]:


arguments = [1, 5, 0, -5, 3, -1]
[(i, j) for i in range() for i in range (len(arguments)) for j in range (len(arguments)) if arguments[i] + arguments[j] == 0]


# In[ ]:


# "try and raise" ?? statement to test the input


# In[ ]:


# 17. Create all possible permutations

"""
is it possible to do (*args) ??
def permute(*args)
    ...
"""

