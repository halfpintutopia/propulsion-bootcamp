
# coding: utf-8

# In[10]:


# Create a set comprehension for all x in 0...9 for the function f(x)=x*x
n = 10
f = 

# Display the result
print(f)


# In[12]:



print({x: x*x for x in range(1, n+1)})


# In[22]:


def perfect_bmi():
    weight = float(input("What is your weight in kilograms?"))
    height = float(input("What is your height in metres?"))
    your_bmi = int((weight / height) / height)
    print(weight)
    print(height)
    print(your_bmi)
    
    if your_bmi < 18.5:
        return "You are underweight"
    elif your_bmi >= 25:
        return "You are overweight"
    elif your_bmi >= 18.5 and your_bmi < 25:
        return "You are normal weight"
        

perfect_bmi()


# In[35]:


num_range = 20
squ_num = [i**2 for i in range(1, num_range+1)]
print(squ_num)
print(squ_num[-5:])


# In[55]:


orders = [
  {
    'id': 'order_001',
    'item': 'Introduction to Python',
    'quantity': 1,
    'price_per_item': 32
  },
  {
    'id': 'order_002',
    'item': 'Advanced Python',
    'quantity': 3,
    'price_per_item': 40

  },
  {
    'id': 'order_003',
    'item': 'Python web frameworks',
    'quantity': 2,
    'price_per_item': 51
  }
]

for key, value in orders.items():
    print (key, value)
 
for key in orders.iterkeys():
    print (key)
     
for value in orders.itervalues():
    print (value)



# In[44]:


# for key, value in orders.items():
#   print(key, value)

for key, value in orders.items():
  print(key, value)


# In[ ]:


def rental_car_cost(days):
  cost = 40 * days
  if days >= 7:
    print(cost - 50) 
  elif (days < 7) and (days >= 3):
    print(cost - 20)
    
print(rental_car_cost(4))

