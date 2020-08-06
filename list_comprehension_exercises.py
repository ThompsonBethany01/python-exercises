#!/usr/bin/env python
# coding: utf-8

# In[11]:


# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())


# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

# In[93]:


upper_fruits = [fruit.upper() for fruit in fruits]
upper_fruits


# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
# 

# In[94]:


capitalized_fruits = [fruit.capitalize() for fruit in fruits]
capitalized_fruits


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

# In[95]:


def count_vowels(string):
    count = 0
    vowels = set("aeiouAEIOU")
    for ch in string:
        if ch in vowels:
            count = count + 1
    return count

fruits_with_more_than_two_vowels = [x for x in fruits if count_vowels(x) > 2]
fruits_with_more_than_two_vowels


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

# In[96]:


def count_vowels(string):
    count = 0
    vowels = set("aeiouAEIOU")
    for ch in string:
        if ch in vowels:
            count = count + 1
    return count

fruits_with_only_two_vowels = [x for x in fruits if count_vowels(x) == 2]
fruits_with_only_two_vowels


# Exercise 5 - make a list that contains each fruit with more than 5 characters

# In[97]:


fruits_with_more_than_5_char = [fruit for fruit in fruits if len(fruit) > 5]
fruits_with_more_than_5_char


# Exercise 6 - make a list that contains each fruit with exactly 5 characters

# In[98]:


fruits_with_exactly_5_char = [fruit for fruit in fruits if len(fruit) == 5]
fruits_with_exactly_5_char


# Exercise 7 - Make a list that contains fruits that have less than 5 characters

# In[99]:


fruits_with_less_than_5_char = [fruit for fruit in fruits if len(fruit) < 5]
fruits_with_less_than_5_char


# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
# 

# In[100]:


length_of_fruits = [len(fruit) for fruit in fruits]
length_of_fruits


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

# In[101]:


def count_a(string):
    count = 0
    set_a = set("aA")
    for ch in string:
        if ch in set_a:
            count = count + 1
    return count

fruits_with_letter_a = [x for x in fruits if count_a(x) > 0]
fruits_with_letter_a


# Exercise 10 - Make a variable named even_numbers that holds only the even numbers

# In[103]:


even_numbers = [x for x in numbers if x % 2 == 0]
even_numbers


# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

# In[24]:


odd_numbers = [x for x in numbers if x % 2 == 1]
odd_numbers


# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

# In[106]:


positive_numbers = [x for x in numbers if x > 0]
positive_numbers


# In[25]:


positive_numbers2 = [x for x in numbers if '-' not in str(x)]
positive_numbers2


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

# In[107]:


negative_numbers = [x for x in numbers if x < 0]
negative_numbers


# In[23]:


negative_numbers2 = [x for x in numbers if '-' in str(x)]
negative_numbers2


# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

# In[114]:


two_or_more_digits = [x for x in numbers if x > 9 or x < -9]
two_or_more_digits


# In[29]:


two_or_more_digits = [x for x in numbers if len(str(abs(x))) >= 2]
two_or_more_digits


# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

# In[115]:


numbers_squared = [x ** 2 for x in numbers]
numbers_squared


# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

# In[118]:


odd_neg_numbers = [x for x in numbers if x % 2 == 1 and x < 0]
odd_neg_numbers


# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five.

# In[120]:


numbers_plus_five = [x + 5 for x in numbers]
numbers_plus_five


# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.

# In[16]:


# creating function first, to count how many factors a number has
def prime_number(number):
    num = [n for n in range(1,101)]
    count = 0
    for n in num:
        if number % n == 0:
            count = count + 1
    return count

prime_number(9)


# In[37]:


# if a number is prime, it only has 2 factors
# count will be 2 for prime numbers
def prime_number(number):
    num = [n for n in range(1,101)]
    count = 0
    for n in num:
        if number % n == 0:
            count = count + 1
    return count

# list comprehension filters out any numbers with more than two factors, aka non prime numbers
primes = [num for num in numbers if prime_number(num) == 2]
primes


# In[41]:


# if a number is prime, it only has 2 factors
# count will be 2 for prime numbers

def prime_number(number):
    num = [n for n in range(1,101)]
    count = 0
    for n in num:
        if number > 0:
            if number % n == 0:
                count = count + 1
    return count

# list comprehension filters out any numbers with more than two factors, aka non prime numbers
primes = [num for num in numbers if prime_number(num) == 2]
primes

