#!/usr/bin/env python
# coding: utf-8

# # Conditional Basics

# prompt the user for a day of the week, print out whether the day is Monday or not

# In[9]:

print('Question 1.')
#input asks user a question, and will store their answer in the varaible created
day = input("What day of the week is it? ")


# In[10]:


#conditional to check if monday or not
if day.lower() == 'monday':
    print(f"Today is {day}!")
else:
    print("Today is not Monday!")


# prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# In[4]:

print('Question 2')
#variable created with user input
day2 = input("What day is today? ")


# In[5]:


#conditional checks if a weekend day, Sat or Sun
if day2.lower() == 'saturday' or day2.lower() == 'sunday':
    print("Today is the weekend!")
else:
    print("Today is not the weekend... :(")


# create variables and make up values for
# 
# - the number of hours worked in one week
# - the hourly rate
# - how much the week's paycheck will be
# - write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

# In[10]:

print('Question 3')
#weekly_hours and hourly_pay are made up values, can change
weekly_hours = 41
hourly_pay = 15

#paycheck is set as hours * pay, will change in conditional if overtime reached
paycheck = weekly_hours * hourly_pay

#if no overtime, prints paycheck
if weekly_hours <= 40:
    print(paycheck)

#if overtime, adds to paycheck before printing
elif weekly_hours >= 41:
    paycheck *= 1.5
    print(paycheck)


# # Loop Basics

# ### While

# Create an integer variable i with a value of 5.

# In[1]:


#sets varialbe to i
i = 5


# Create a while loop that runs so long as i is less than or equal to 15. Each loop iteration, output the current value of i, then increment i by one.
# Your output should look like this:
# 
# 
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15

# In[2]:

print('Question 4')
#prints i while less than 16, adds one per loop
while i <= 15:
    print(i)
    i += 1


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

# In[2]:

print('Question 5')
#starts count at 0
count = 0

#counts up to 100
while count <= 100:
    print(count)
    #increments by 2
    count += 2


# Alter your loop to count backwards by 5's from 100 to -10.

# In[3]:

print('Question 6')
#starts count at 100
count = 100

#ends count at -10
while count >= -10:
    print(count)
    #increments down by 5
    count += -5


# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
# 
#  2
#  4
#  16
#  256
#  65536

# In[12]:

print('Question 7')
#starts loop at 2
x = 2

#conditional so value is less than 1,000,000
while x < 1_000_000:
    print(x)
    #sets new value to x ** 2 before loop continues
    x = x ** 2


# Write a loop that uses print to create the output shown below.
# 
# 
# 100
# 95
# 90
# 85
# 80
# 75
# 70
# 65
# 60
# 55
# 50
# 45
# 40
# 35
# 30
# 25
# 20
# 15
# 10
# 5

# In[1]:

print('Question 8')
#starts at 100
x = 100

#ends at 5
while x <= 100 and x >= 5:
    print(x)
    #increments by negative 5
    x -= 5


# ### For Loops

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
# 
# For example, if the user enters 7, your program should output:
# 
# 
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70
# 

# In[11]:

print('Question 9')
#user input for number variable
num = input("Enter a number: ")

#multiplication table starts at 1
count = 1

#ends at 10
while count <= 10:
    
    #product of multiplying at each loop... 7 x 1, 7 x 2, etc.
    result = int(num) * count
    
    #string formatting to print num variable with count of loop and result
    print(f'{num} x {count} = {result}')
    count += 1


# Create a for loop that uses print to create the output shown below.
# 
# 
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
# 

# In[2]:

print('Question 10')
#for loop of range 1, 10
for i in range(10):
    #prints string times loop index
    print(str(i) * i)


# ### Break and continue

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
# 
# Your output should look like this:
# 
# 
# Number to skip is: 27
# 
# Here is an odd number: 1
# Here is an odd number: 3
# Here is an odd number: 5
# Here is an odd number: 7
# Here is an odd number: 9
# Here is an odd number: 11
# Here is an odd number: 13
# Here is an odd number: 15
# Here is an odd number: 17
# Here is an odd number: 19
# Here is an odd number: 21
# Here is an odd number: 23
# Here is an odd number: 25
# Yikes! Skipping number: 27
# Here is an odd number: 29
# Here is an odd number: 31
# Here is an odd number: 33
# Here is an odd number: 35
# Here is an odd number: 37
# Here is an odd number: 39
# Here is an odd number: 41
# Here is an odd number: 43
# Here is an odd number: 45
# Here is an odd number: 47
# Here is an odd number: 49

# In[13]:

print('Question 11')
#answering without break and continue
#user input to decide which number to skip
num = input("Choose an odd number to skip: ")

#variable for start of loop
x = 1

#loops until 50
while x <= 50:
    
    #checks if wrong input, keeps asking for new input
    while num.isdigit() == False or int(num) % 2 == 0 or int(num) < 1:
        print('Incorrect input, heathen!')
        num = input("Choose an odd number to skip: ")
    
    #prints as long as not skipped number
    print(f'Here is an odd number: {x}')
    #increments by two for odd numbers
    x += 2

    #If input is num, prints different statement
    if x == int(num):
        print(f'Yikes! Skipping number: {num}')
        #increments by two for odd numbers
        x += 2
              


# In[1]:

print('Alternative Code')
#answering with break and continue
#user input to decide which number to skip
num = input("Choose an odd number to skip: ")

#loops through range 1 to 50
for n in range(1, 51, 2):
    
    #asks for input while input is incorrect, breaks loop when correct input
    while num.isdigit() == False or int(num) % 2 == 0 or int(num) < 1:
        print('Incorrect input, heathen!')
        num = input("Choose an odd number to skip: ")
        if num.isdigit() == True and int(num) % 2 != 0 and int(num) > 0:
            break
        
    #conditional for skipped number
    if n == int(num):
        print(f'Yikes! Skipping number: {num}')
        continue
        
    print(f'Here is an odd number: {n}')


# The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

# In[33]:

print('Question 12')
#user input for positive number
num = input("Enter a positive number: ")

#continues to ask while incorrect input
while num.isdigit() == False or int(num) <= 0:
        print('Incorrect input, heathen!')
        num = input("Enter a positive number: ")
        if num.isdigit() == True or int(num) > 0:
            break
            
#prints from 0 to chosen number            
for x in range(0,int(num) + 1):
    print(x)
    x += 1


# Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

# In[17]:

print('Question 13')
#input for positive number
num = input("Enter a positive number: ")

#if incorrect input, continues to ask
while num.isdigit() == False or int(num) <= 0:
        print('Incorrect input, heathen!')
        num = input("Enter a positive number: ")
        if num.isdigit() == True or int(num) >= 1:
            break
            
#loop to count down from num to zero
for x in range(int(num), 0, -1):
    print(x)


# # Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# 
# - Write a program that prints the numbers from 1 to 100.
# - For multiples of three print "Fizz" instead of the number
# - For the multiples of five print "Buzz".
# - For numbers which are multiples of both three and five print "FizzBuzz".

# In[36]:

print('Question 14')
#prints range from 1 to 100
for x in range(1, 101):
    
    #conditional for multiples of 3 and 5 first
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
        
    #conditional for multiples of 3
    elif x % 3 == 0:
        print('Fizz')
        
    #conditional for multiples of 5
    elif x % 5 == 0:
        print('Buzz')
        
    #if no condtionals met, prints number
    print(x)


# # Display a table of powers.

# Prompt the user to enter an integer.
# - Display a table of squares and cubes from 1 to the value entered.
# - Ask if the user wants to continue.
# - Assume that the user will enter valid data.
# - Only continue if the user agrees to.
# 
# Example Output
# 
# What number would you like to go up to? 5
# 
# Here is your table!
# 
# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125

# In[83]:

print('Question 15')
#user input for number
num = input('Enter an integer: ')

#prints name of columns
print('number - squared - cubed')

#prints values in same line
for x in range(1, int(num) + 1):
    print(f'   {x}        {x ** 2}        {x ** 3}') 
    
#continues based on input
cont = input('Do you wish to continue, Y or N: ')

while cont == 'Y':
    
    num = input('Enter an integer: ')

    print('number - squared - cubed')
    for x in range(1, int(num) + 1):
        print(f'   {x}        {x ** 2}        {x ** 3}')
        
    cont = input('Do you wish to continue, Y or N: ')

#says goodbye when program ends
print('Goodbye')


# Bonus: Research python's format string specifiers to align the table

# In[66]:

print('Working on bonus Question 15')
#still working on bonus
num = input('Enter an integer: ')
mylist = []
print('number - squared - cubed')
for x in range(1, int(num) + 1):
    new = [x, x ** 2, x ** 3]
    mylist.append(new) 

print(mylist)


# # Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# - Display the corresponding letter grade.
# - Prompt the user to continue.
# - Assume that the user will enter valid integers for the grades.
# - The application should only continue if the user agrees to.
# 
# Grade Ranges:
# 
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

# In[25]:

print('Question 16')
#checks conditionals based on grade input
grade = input("Enter a grade between 0 and 100: ")

if 100 >= int(grade) >= 88:
    print('A')
    
if 87 >= int(grade) >= 80:
    print('B')
    
if 79 >= int(grade) >= 67:
    print('C')
    
if 66 >= int(grade) >= 60:
    print('D')
    
if 59 >= int(grade) >= 0:
    print('F')


# Bonus
# 
# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

# In[29]:

print('Bonus Question 16')
#checks conditionals based on grade
grade = input("Enter a grade between 0 and 100: ")
#converts to integer
grade = int(grade)

if 100 >= grade >= 88:
    if grade > 98:
        print('A+')
    elif grade < 92:
        print('A-')
    else:
        print('A')
    
if 87 >= grade >= 80:
    if grade > 85:
        print('B+')
    elif grade < 82:
        print('B-')
    else:
        print('B')
    
if 79 >= grade >= 67:
    if grade > 77:
        print('C+')
    elif grade < 69:
        print('C-')
    else:
        print('C')
    
if 66 >= grade >= 60:
    if grade > 64:
        print('D+')
    elif grade < 62:
        print('D-')
    else:
        print('D')
    
if 59 >= grade >= 0:
    if grade > 57:
        print('F+')
    elif grade < 62:
        print('F-')
    else:
        print('F')


# # Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.

# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# In[8]:

print('Question 17')
#user chooses genres
genre = input("Enter a genre of books: ")
#empty count variable
count = 0

#checks if book match genre regardless of capitalized spelling
for x in books:
    if genre.upper() == x['genre'].upper():
        print(f'One book is: {x}')
        #if book found, count goes up
        count += 1

#prints if no book in that genre found, aka count still equals 0
if count == 0:
    print("No such books in my list.")


# In[2]:


books = [
    {
        "title": "Ender's Game",
        "genre": "Science Fiction",
        "author": "Orson Scott Card"
    },
    {
        "title": "Outermen",
        "genre": "Science Fiction",
        "author": "BP Gregory"
    },
    {
        "title": "The Time Machine",
        "genre": "Science Fiction",
        "author": "HG Wells"
    },
    {
        "title": "Twilight",
        "genre": "YA Fiction",
        "author": "Stephanie Meyer"
    },
    {
        "title": "Oh the Places You'll Go",
        "genre": "Children",
        "author": "Dr. Suess"
    }
]

