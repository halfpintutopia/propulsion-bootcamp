
# coding: utf-8

# In[4]:


def say_hello(name):
    print ("Hello {}\".format(name))

say_hello("Laurent") # => Hello Laurent
say_hello("Simon")   # => Hello Simon
say_hello("Class")   # => Hello Class


# In[5]:


def describe_movie(title, genre):
    return "{} is a {} movie".format(title, genre)

# correct
print(describe_movie('Star Wars: Episode IV - A New Hope', 'Action, Adventure, Fantasy'))

# arguments order switched around --> wrong result
print(describe_movie('Action, Adventure, Fantasy', 'Star Wars: Episode IV - A New Hope'))


# In[6]:


def describe_movie(title, genre):
    return "{} is a {} movie".format(title, genre)

# correct
print(describe_movie(title='Star Wars: Episode IV - A New Hope', genre='Action, Adventure, Fantasy'))

# argument order switched around -> correct, because we are using keyword arguments
print(describe_movie(genre='Action, Adventure, Fantasy', title='Star Wars: Episode IV - A New Hope'))


# In[ ]:


def sum(*args):
    # counter
    result = 0
    for num in args:
        # add next indexed number to the counter
        result = result + num
    return result

sum()      # -> 0
sum(10)    # -> 10
sum(1,2)   # -> 3
sum(1,2,3) # -> 6

