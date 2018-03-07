"""
Exercises day 2
1. Filter, map, and lambda exercises
1.1 Even numbers
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.
"""
li1 = [1,2,3,4,5,6,7,8,9,10]
print(list(filter((lambda num: num%2==0), li1)))


"""
1.2 Square elements
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use lambda to define anonymous functions.
"""
li2 = [1,2,3,4,5,6,7,8,9,10]
print(list(map((lambda num: sqrt(num)), li2)))


"""
1.3 Squared even numbers
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.
"""
list(map(filter(lambda num: sqrt(num).is_integer() or num%2==0)))


"""
1.4 Find certain numbers
Write a function find_numbers(min, max) that will find all numbers that are a multiple of 7 but not a multiple of 5.

First, try getting it right with an explicit for loop. If you have it up and running, write a second version that avoids explicit for loops and uses filter and lambda only!
"""
# explicit with for loop
def find_numbers(min, max):
    rangeof_nums = list(range(min, max))
    div7 = []
    for i in rangeof_nums:
        if i % 7 == 0 and i % 5 != 0:
            div7.append(i)
    return div7

find_numbers(2, 40)


# filter and lambda
list(filter(lambda  num: (num % 7 == 0 and num % 5 != 0),list(range(min, max))))


"""
2. Webstore
Assume you have a web store, and you have list of orders like the following:

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
You don't like that people order in small quantities, which is why you would like to add a CHF 10 addition to the total price, for all orders that are below CHF 100 in total.

Write a short Python function compute_totals that returns a list of 2-tuples. Each tuple consists of the order number and the total price (number of items times price per item). The total price should be increased by CHF 10 if the total is less than CHF 100.

Again - try to first get it right using an explicit for loop, and then try to optimize using map and lambda!

The result should look like this:

totals = compute_totals(orders)
# result is [('order_001', 42), ('order_002', 120), ('order_003', 102)]
"""
def compute_totals(orders):
    for i in orders

"""
3. Input and range
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

# result
# for n=10:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

"""
# Generate a dictionary that contains (i, i*i) with integral number between 1 and n (inclusive)
n = 10
print({x: x*x for x in range(1, n + 1)})


"""
4.List comprehensions
Using List comprehensions generate a list where the values are square of numbers between 1 and 20 (both included). The print the last 5 elements in the list.

# result [256, 289, 324, 361, 400]
"""
# list comprehension
# [i*2 for i in range(4)]

num_range = 20
squ_num = [i**2 for i in range(1, num_range+1)]
# print(squ_num)

print(squ_num[-5:])


"""
5. Print style
Write a small script that will print numbers 1-10 in a way that if the number is even it prints the number, if the number is odd it print underscore _:

Hint: check the arguments for the print() function.

# result _2_4_6_8_10
"""
print(list(map(lambda i: "_"*(i%2!=0) or str(i), range(10))))


"""
6. BMI calculator
The first exercise for today is going to be the BMI calculator

Print "Let's calculate your BMI (kg/m^2)" to the console.
Ask the user about the weight in KG.
Ask the user about the height in CM.
Read the users weight as a float.
Read the users height.
A function to calculate the BMI and show info if they are underweight, overweight or normal weight.
"""
def perfect_bmi():
    weight = float(input("What is your weight in kilograms?"))
    height = float(input("What is your height in metres?"))
    your_bmi = int((weight / height) / height)
    # print(weight)
    # print(height)
    # print(your_bmi)

    if your_bmi < 18.5:
        return "You are underweight"
    elif your_bmi >= 25:
        return "You are overweight"
    elif your_bmi >= 18.5 and your_bmi < 25:
        return "You are normal weight"

perfect_bmi()


"""
7. Shopping list.
What am I buying?
Create a shopping list app, in which the user can add and remove items from his shopping list using the console.

Create a function called help_menu() which basically is going to show the users a help menu for you simple app:
Example: Press 'a' to add items to the shopping list. Press 's' to show the items in the list, 'r' to remove and 'q to quit the app'
Create a function show_items() which reads the list and shows the items to the user, items should have an order numbers too.

Create a function add_item() which allows the user to add a new item to the list. Ask the user for the position of the item when adding, if None add the item to the end of the list.

Create a function remove_item() to remove an item form the list

Example flow through the app:

        Press 'h' for help menu
        Press 's' to show the item in your list
        Press 'a' to add a new item to the list
        Press 'r' to remove an item from the list
        Press 'q' to quit
What do you want to do? s
There are no items on the list!

What do you want to do? a
What do you want to add? Milk

What do you want to do? s
1: Milk
2: Beer

What do you want to do?
"""
#record of shopping list items
shopping_list = []

#ask for new item
new_item = input("> ")


#quit the app:
quit = str(input("Press 'q' to quit"))
if new_item == "q":
    break

#add new items to shopping list
shopping_list.append(new_item)

#delete items from your shopping list
index_of_item = int(input("Where would you like to add your item to the list. Please choose between 1 - " + str(len(shopping_list)+1)))
shopping_list.remove(item)

#shows you your list
print("Here's your list")

#printing out the items
for item in shopping_list: print(item)


"""
8. Number guess game
In this exercise we will build a simple game that lets the user guess a random number.

Create a function start() that will start the game
A function called play_again() which will ask the users they want to play again when the game ends.
Print 'I am thinking of a number from 1-10. Can you find it? You have 5 tries.'
Check if the input of the user is an int.
Create an infinite loop to allow the users to guess multiply times Within the loop...
Print "Guess what it is: ".
Read in the user's guess as an int.
If the user guessed correctly, print *"Congratulations! You guessed it.Ask the user if he/she wants to play again..
If the user's guess is lower than the random number, print "Nope. It's lower than that. Try again." to the console.
If the user's guess is higher than the random number, print "Nope. It's higher than that. Try again." to the console.
Track how many guesses the user has made and print "Congratulations! You guessed it in # tries." to the console if the user guesses correctly, where # is the number of guesses.
"""
# import random
n = random.randint(1, 11)
guess = int(raw_input("I am thinking of a number from 1 - 10. Can you find it. You have 5 tries"))

def guess():
    int(raw_input("I am thinking of a number from 1 - 10. Can you find it. You have 5 tries"))

def incorrect_toolow():
    print("Nope. It's higher than that. Try again.")

def incorrect_toohigh():
    print("Nope. It's lower than that. Try again.")


while n != "guess":
    # print
    if guess < n:
        # print "Nope. It's higher than that. Try again."
        incorrect_toolow()
        guess()

"""
Bonus
9. Hangman
In this exercise we are going to build the old hangman game. For this one we are using this file as a data source.

First try to read the file using open() function from python.
Create a function to get the user's input, take into account that the user is allowed to type a letter at a time. No numbers or words.
If the user types the same letter over again, let the user know he used that letter already.
The user is allowed to guess only 7 times wrong.
Print the information every time the user guesses a letter. For example:
only for testing purposes, the word is ->  other

        To quit the game simply type 'quit'.
        You only have 7 tries for this game.

 _ _ _ _ _
You have 0/7 tries left

Write your letter:  o
o _ _ _ _
You have 0/7 tries left

Write your letter:  t
ot _ _ _
You have 0/7 tries left

Write your letter:  r
ot _ _r
You have 0/7 tries left

Write your letter:
Count the wrong letter and let the user know about the wrong guesses.
If the user wins or losses ask to play again.
"""