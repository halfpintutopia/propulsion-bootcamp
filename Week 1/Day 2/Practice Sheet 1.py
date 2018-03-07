
# coding: utf-8

# In[15]:


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

[order for order, price in orders.items() if price == price_per_item]


# In[2]:


orders


# In[10]:


list(1, 4)


# In[12]:


list("6")


# In[14]:


list(range(2, 4))


# In[31]:


li3 = [1,2,3,4,5,6,7,8,9,10]
# list(map(filter(lambda num: (num**num).is_integer() or num%2==0)))

list(filter((lambda num: (num**num).is_integer() or num%2==0), li3))


# In[32]:


list(filter(lambda  num: (num % 7 == 0 and num % 5 != 0),list(range(2, 40))))


# In[27]:


def input_range(n, **kwargs):
    num_dict = {}
    # user["name"] = name
    # user["password"] = password
    for i in kwargs.items():
        num_dict[i] = i*i

    return num_dict

input_range(9)


# In[33]:


def rangeof_Nums(n):
    num_dict= {}
    for i in n:
        num_dict[i] = i*i
        
    return num_dict

input_range(9)


# In[36]:


def underscored(num):
    rangeof_nums = (list(num))
    underscored_nums = []
    for check in rangeof_nums:
        if rangeof_nums(check) % 2 != 0:
            underscored_nums += check
        else:
            underscored_nums += check
    return underscored_nums
            
underscored(10)


# In[ ]:


def perfect_bmi():
    weight = float(input("What is your weight in kilograms?"))
    height = float(input("What is your height in centimetres?"))
    your_bmi = (weight / height) / height

    if bmi >= 18.5 and bmi < 25:
        return "You are normal weight"
    elif bmi >= 25 and bmi < 30:
        return "You are overweight"
    elif bmi < 18.5:
        return "You are underweight"


# In[ ]:


def perfect_bmi():
    weight = float(input("What is your weight in kilograms?"))
    height = float(input("What is your height in metres?"))
    your_bmi = (weight / height) / height

    if your_bmi >= 18.5 and your_bmi < 25:
        return "You are normal weight"
    elif your_bmi >= 25 and your_bmi < 30:
        return "You are overweight"
    elif your_bmi < 18.5:
        return "You are underweight"

perfect_bmi()


# In[48]:


def underscored(start, end):
    rangeof_nums = list(range(start, end))
    underscored_nums = []
    for check in rangeof_nums:
        if rangeof_nums(check) % 2 != 0:
            underscored_nums += check
        else:
            underscored_nums += check

underscored(1, 10)


# In[50]:


list(range(1, 10+1))


# ### def start():
#     my_number = int(input("Which number should the player be guessing?"))
#     your_guess = int(input("I am thinking of a number from 1-10. Can you find it? You have 5 tries. Guess what is it"))
#     tries = 1
#     while your_guess != my_number:
#         if your_guess != my_number:
#             if your_guess < my_number:
#                 tries += 1
#                 return "Nope. It's higher than that. Try again." 
#             elif your_guess > my_number:
#                 tries += 1
#                 return "Nope. It's lower than that. Try again."
#      
#         else: 
#             return f"Congratulations! You guessed it in {tries} tries."
#     
# def play_again():
#     answer = input("Do you want to play again? Y or N")
#     if answer == "Y":
#         start()
#     else:
#         return "Thank you for playing!"
#     
# start()

# def start():
# my_number = int(input("Which number should the player be guessing?"))
# your_guess = int(input("I am thinking of a number from 1-10. Can you find it? You have 5 tries. Guess what is it"))
# tries = 1
# while your_guess != my_number:
#     if your_guess != my_number:
#         if your_guess < my_number:
#             tries += 1
#             return "Nope. It's higher than that. Try again." 
#         elif your_guess > my_number:
#             tries += 1
#             return "Nope. It's lower than that. Try again."
# 
#     else: 
#         return f"Congratulations! You guessed it in {tries} tries."
# def play_again(): answer = input("Do you want to play again? Y or N") if answer == "Y": start() else: return "Thank you for playing!"
# 
# start()

# In[60]:


def start():
    my_number = int(input("Which number should the player be guessing?"))
    your_guess = int(input("I am thinking of a number from 1-10. Can you find it? You have 5 tries. Guess what is it"))
    tries = 1
    while False:
        if your_guess != my_number:
            if your_guess < my_number:
                tries += 1
                return "Nope. It's higher than that. Try again." 
            elif your_guess > my_number:
                tries += 1
                return "Nope. It's lower than that. Try again."

        else: 
            return f"Congratulations! You guessed it in {tries} tries."

def play_again(): 
    answer = input("Do you want to play again? Y or N") 
    if answer == "Y": 
        start() 
    else: 
        return "Thank you for playing!"

start()


# In[ ]:


def start():
    my_number = int(input("Which number should the player be guessing?"))
    your_guess = int(input("I am thinking of a number from 1-10. Can you find it? You have 5 tries. Guess what is it"))
    tries = 1
#     while False:
    if your_guess != my_number:
        if your_guess < my_number:
            tries += 1
            return "Nope. It's higher than that. Try again."
        elif your_guess > my_number:
            tries += 1
            return "Nope. It's lower than that. Try again."
    else:
        return f"Congratulations! You guessed it in {tries} tries."

def play_again():
    answer = input("Do you want to play again? Y or N")
    if answer == "Y":
        start()
    else:
        return "Thank you for playing!"

    
start()


# In[ ]:


def start():
    my_number = 6
    your_guess = int(input("I am thinking of a number from 1-10. Can you find it? You have 5 tries. Guess what is it"))
    tries = 0
    if your_guess != my_number:
        if your_guess < my_number:
            tries += 1
            return "Nope. It's higher than that. Try again."
        elif your_guess > my_number:
            tries += 1
            return "Nope. It's lower than that. Try again."
    else:
        return f"Congratulations! You guessed it in {tries} tries."

def play_again():
    answer = input("Do you want to play again? Y or N")
    if answer == "Y":
        start()
    else:
        return "Thank you for playing!"
    
start()


# In[ ]:


import random
print random.randint(0, 5)


# In[ ]:


print random.randint(0, 5)


# In[ ]:


def start():
    my_number = int(input("What's the number?"))
    your_guess = int(input("I am thinking of a number from 1-10. Can you find it? You have 5 tries. Guess what is it"))
    tries = 1
    while your_guess != my_number
        if your_guess != my_number:
            if your_guess < my_number:
                tries += 1
                return "Nope. It's higher than that. Try again."
            elif your_guess > my_number:
                tries += 1
                return "Nope. It's lower than that. Try again."
        else:
            return f"Congratulations! You guessed it in {tries} tries."

def play_again():
    answer = input("Do you want to play again? Y or N")
    if answer == "Y":
        start()
    else:
        return "Thank you for playing!"
    
start()


# In[ ]:


def underscored(start, end):
    rangeof_nums = list(range(start, end + 1))
    underscored_nums = []
    for check in rangeof_nums:
        if rangeof_nums(check) % 2 != 0:
            underscored_nums += check
        else:
            underscored_nums += check

underscored(1, 10)


# In[ ]:


def underscored(10):
    for items in l:
        print(l, end=' ')
        
value([1, 2, 3, 4])


# In[ ]:


print("Welcome to" , end = ' ') 
print("GeeksforGeeks", end = ' ')


# In[ ]:


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

orders[0]["quantity"]


# In[ ]:


li2 = [1,2,3,4,5,6,7,8,9,10]
print(list(map(filter((lambda num: sqrt(num).is_integer() or num%2==0), li2))))

