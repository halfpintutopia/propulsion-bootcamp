
# coding: utf-8

# In[ ]:


# Default params
def describe_show(title, genre, producer="Netflix", country="US"):
    print(f"Show {title} has genre {}, produced by {producer} in {country}")

describe_show("House of Cards", "Drama, Thriller")
describe_show("Casa de Papel", country="Spain") # error - missing positional argument
describe_show("Spain", "Casa de Papel", "Crime") # error - positional argument follow keyword argument
"""
Don't mix positional and keyword arguments
Start with positional argments
"""


# In[1]:


# variable
def example_vars(*args): # argument in a tuple
    print(args)
    
example_vars("a") 


# In[2]:


def example_vars(*args): # argument in a tuple
    for i, el in enumerate(args):
        print(f"Argument #{i} = {el}")
    
example_vars("a", "b", "c") 


# In[3]:


# enumerate
arr = ["a", "b", "c"]
for el in arr:
    print(el)


# In[ ]:


# any amount of positional arguments
def fun(*args):
    res = 0
    for a in args:
        res += a
    return res

#fun([10, 20, 30]) - error - assumes its one element e.g. fun([10, 20, 30], 10, 5)


# In[4]:


# any amount of vari
def ex_kw(**kwargs):
    for key, val in kwargs.items():
        print(f"Key is {key} has value {val}")
        
ex_kw(twenty=20, thirty=30, one=1)


# In[6]:


def ex_kw_dict(**kwargs):
    print(kwargs)
ex_kw_dict(twenty=20, thirty=30, one=1)


# In[7]:


def make_dicts(**kwargs):
    return kwargs

dict(key1=1, key2=2)


# In[9]:


def create_user(name, password, **kwargs):
    user = {}
    user["name"] = name
    user["password"] = password
    for key, value in kwargs.items():
        user[key] = value
    
    return user

print(create_user("Donald", "asdgfs", full_name="Donald Duck", age="150"))

