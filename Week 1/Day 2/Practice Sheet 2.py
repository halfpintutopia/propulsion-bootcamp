
# coding: utf-8

# In[5]:


def start():
    my_number = int(input("What's the number?"))
    your_guess = int(input("I am thinking of a number from 1-10. Can you find it? You have 5 tries. Guess what is it"))
    tries = 1
    while your_guess != my_number:
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


def value(l):
    for items in l:
        print(l, end=' ')
        
value(["1", "2", "3"])


# In[ ]:


def value(nums):
    for items in nums:
        print(nums, end=" ")
        
value([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# In[ ]:


for i in range(10):
    print("_", end="")
    #val, sep, end
# end="" used for \n newline

#print(list(map((lambda num: num%2!=0), range(11))))


# In[14]:


def underscored(start, end):
    rangeof_nums = list(range(start, end + 1))
    underscored_nums = []
    for check in rangeof_nums:
        if rangeof_nums(check) % 2 != 0:
            underscored_nums += check
        else:
            underscored_nums += check

underscored(1, 10)

list(map(lambda num: num % 2 !=0))


# In[23]:


for x in range(10): 
    if x%2 != 0:
        return "_"
    else:
        return x


# In[24]:


print(list(map(lambda i: "_"*(i%2!=0) or str(i), range(10))))


# In[44]:


print("Welcome to" , end = ' ') 
print("GeeksforGeeks", end = ' ')


# In[48]:


def start():
    my_number = int(input("What's the number?"))
    your_guess = int(input("I am thinking of a number from 1-10. Can you find it? You have 5 tries. Guess what is it"))
    tries = 1
    while True:
        if your_guess != my_number:
            if your_guess < my_number:
                tries += 1
                return "Nope. It's higher than that. Try again."
            elif your_guess > my_number:
                tries += 1
                return "Nope. It's lower than that. Try again."
        else:
            return f"Congratulations! You guessed it in {tries} tries."
        
start()


# In[ ]:


while expression: target = true_expression if test_expression else false_expression


# In[ ]:


while True: your_guess = my_number


# In[ ]:


# my_number = int(input("What's the number?"))

def start():
    my_number = 5
    your_guess = int(input("I am thinking of a number from 1-10. Can you find it? You have 5 tries. Guess what is it"))
    while True: my_number = your_guess if not "Nope. It's higher than that. Try again." else "Nope. It's lower than that. Try again."
    
start()


# In[ ]:


def value(nums):
    for items in nums:
        print(nums, end="")
        
value([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


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

print(orders(0))


# In[ ]:


# Create a set comprehension for all x in 0...9 for the function f(x)=x*x
n = 10
f = {x: x*2 for x in range(n)}

# Display the result
print(f)

