#!/usr/bin/env python
# coding: utf-8

# # 1. Import and test 3 of the functions from your functions exercise file.
# 
# Import each function in a different way:
# 
# import the module and refer to the function with the . syntax
# use from to import the function directly
# use from and give the function a different name

# ### using import file_name

# In[1]:


import function_exercises


# In[3]:


function_exercises.is_two(2)


# ### using import and renaming file

# In[4]:


import function_exercises as fe


# In[8]:


fe.is_vowel('a')


# ### using import on specific function inside the file

# In[9]:


from function_exercises import str_cap


# In[10]:


str_cap('hello')


# ### using import on specific function inside the file and renaming

# In[12]:


from function_exercises import calculate_tip as tip


# In[13]:


tip(.5, 12.99)


# ## For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.

# # 2. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

# In[69]:


#importing functions used to count permutations, combinations, etc
from itertools import product


# In[74]:


#import product allows us to find all the unique combinations of different sets
#'abc' will not be combined with each, same for '123'
print (list(product('abc','123')))

#finds the length of the list of different combinations from product function
#converts this to a str to print out
count = str(len(list(product('abc','123'))))
print ("There are " + count + " different ways to combine the letters 'abc' with the numbers '123'.")


# # 3. How many different ways can you combine two of the letters from "abcd"?

# In[79]:


#importing the combination function specifically and renamed as c
from itertools import combinations as c


# In[81]:


#we call the imported function with its alias
#the output is a list of the different combinations
print (list(c(['a','b','c','d'], 2)))

#to find the amount of combinations, we take the length of the list
#this is converted to a string for output
count = str(len(list(c(['a','b','c','d'], 2))))
print(("There are " + count + " different ways to combine the letters 'abcd' by two with each other."))


# Save this file as profiles.json inside of your exercises directory.

# # Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
# 
# - Total number of users
# - Number of active users
# - Number of inactive users
# - Grand total of balances for all users
# - Average balance per user
# - User with the lowest balance
# - User with the highest balance
# - Most common favorite fruit
# - Least most common favorite fruit
# - Total number of unread messages for all users

# In[3]:


#importing module to read json file
import json


# In[4]:


#opens json file and stores it in a variable
with open('profiles.json') as f:
  data = json.load(f)


# In[125]:


#defines a function that counts the total users in the file
def count_users(user_data):
    
    #each entry in the list is a dictionary of a users information
    #the length of this list returns the amount of users
    users = len(data)
    print('The total number of active and inactive users is: ' + str(users))
    return users


# In[126]:


count_users(data)


# In[127]:


#defines a function that counts the total of active users
def active_count(user_data):
    
    #sets empty count variable
    count = 0
    
    #iterates through each user in the file
    for x in user_data:
        #adds to the count if active, aka isActive is True
        if x["isActive"] == True:
            count += 1
            
    print('The total number of active users is: ' + str(count))
    return count


# In[128]:


active_count(data)


# In[129]:


#defines a function that counts the total of inactive users
def inactive_count(user_data):
    #sets an empty count variable
    count = 0
    
    #iterates through each user in the file
    for x in user_data:
        #adds to count if the user is inactive
        if x["isActive"] == False:
            count += 1
    print('The total number of inactive users is: ' + str(count))
    return count


# In[130]:


inactive_count(data)


# In[145]:


#defines a function that totals the balances of all users
def total_balances(user_data):
    
    #sets an empty total variable
    total = 0
    
    #iterates through each user in the file
    for x in user_data:
        
        #stores the individual user balance in variable
        bal_str = x['balance']
        
        #sets an empty variable to store the balance as a float later
        bal_float = ''
        
        #iterates through the characters in the blance string
        for y in bal_str:
            
            #only adds char to string if the value is a number or decimal
            if y != '$' and y != ",":
                bal_float = bal_float + y
        
        #converts the balance to a float
        bal_float = float(bal_float)
        
        #adds the balance to the total
        total += bal_float
        
        #formats back to string in dollar format
        total_str = "${:,.2f}".format(total)
        
    print('The total amount of balances owed amoung users is: ' + str(total_str))
    
    #returns original float value
    return total


# In[146]:


total_balances(data)


# In[147]:


#defines a function to determine the average balance owed amoung all users
def avg_balance(user_data):
    
    #sets total balance owed using function defined earlier
    total = total_balances(user_data)
    
    #sets total users using function defined earlier
    users = count_users(user_data)
    
    #calculates average by total balance owed divided by total users
    avg = total / users
    
    #formats to string in dollar format
    avg_str = "${:,.2f}".format(avg)
    print('The average balance amoung all users is: ' + str(avg_str))
    
    #returns average in original float value
    return avg


# In[148]:


avg_balance(data)


# In[176]:


#defines a function to determine the lowest balance owed
def lowest_balance(user_data):
    
    #iterates through users in file
    for x in user_data:
        #creates first balance for comparison to other balances
        #whether or not it is the lowest is determined below
        #cannot set the variable to 0, because no balance is lower than 0
        low = x['balance']
        #stops because we only need one value
        break
    
    #iterates through the users again
    for x in user_data:
        #checks to see if lower than first balance
        if x['balance'] < low:
            #if lower, it sets that to the new low amount
            low = x['balance']
    
    #no addition or subtraction is done, so no converting to integer was needed
    #the variable stayed a string
    print('The lowest balance amoung all users is: ' + low)
    return low


# In[177]:


lowest_balance(data)


# In[178]:


#defines a function to find lowest balance owed
def highest_balance(user_data):
    
    #iterates through users in file
    for x in user_data:
        #sets first balance to variable for comparison later
        #does not need to be the highest, we will determine that below
        high = x['balance']
        #break because we only need one value
        break
        
    #iterates through users again
    for x in user_data:
        #if value is higher, we reassign the variable
        if x['balance'] > high:
            high = x['balance']
    
    #no addition or subtraction is done, so no converting to integer was needed
    #the variable stayed a string
    print('The highest balance amoung all users is: ' + high)
    return high


# In[179]:


highest_balance(data)


# In[5]:


#the follwing function is the first step in determing what fruits are the favorite and least favorite
def fruit_list(user_data):
    #sets an empty list to add the names too
    fruits = []
    
    #iterates through the users in the file
    for x in user_data:
        #adds to the list if in favoriteFruit column
        fruits.append(x['favoriteFruit'])
    return fruits


# In[6]:


fruit_list(data)


# In[181]:


#this function counts how many of each fruit is a favorite into a dictionary
def fruit_count(user_data):
    
    #sets an empty dictionary to add the fruit names and counts to
    fruits = {}
    
    #iterates through the users
    for x in user_data:
        #adds the fruit name to the dictionary if not already added
        fruits.update( {x['favoriteFruit'] : 0} )
        
    #iterates through the dictionary fruits we just created
    for y in fruits:
        #sets empty count variable for each fruit name
        count = 0
        #iterates through the fruits in each user
        for x in user_data:
            #if the value matched the fruit in fruits, it adds to the count
            if y == x['favoriteFruit']:
                count += 1
        #the count is updated for each fruit name, then set back to 0 for the next one
        fruits.update( {y : count} )   
        
    return fruits


# In[182]:


fruit_count(data)


# In[183]:


#this function takes the dictionary we created above to find the most favorite
def fav_fruit(user_data):
    
    #we create the fruits dictionary with the function above
    fruits = fruit_count(data)
    
    #we cannot just do max(dictionary), this returns the max key name, not value
    #this line finds the max based on the key value, then returns the key name associated with it
    max_key = max(fruits, key=lambda k: fruits[k])
    return max_key


# In[184]:


fav_fruit(data)


# In[185]:


#this function takes the dictionary we created above to find the least favorite
def least_fav_fruit(user_data):
    
    #we create the fruits dictionary with a previous function
    fruits = fruit_count(data)
    
    #we cannot just do min(dictionary), this returns the min key name, not value
    #this line finds the min based on the key value, then returns the key name associated with it
    min_key = min(fruits, key=lambda k: fruits[k])
    return min_key


# In[186]:


least_fav_fruit(data)


# In[114]:


#this function counts the total amount of unread messages amoung all users
def unread_messages(user_data):
    
    #creates a set of all numbers, to compare with later
    numbers = set('1234567890')
    
    #sets empty count variable
    count = 0
    
    #iterates through each user in the file
    for x in user_data:
        
        #only checks message count if unread
        if 'unread' in x['greeting']:
            
            #sets empty variable for number as string
            number = ''
            
            #iterates through each character in the greeting string
            for char in x['greeting']:
                #only adds char to number if in set numbers, ignores other characters
                if char in numbers:
                    number = number + char
                    
            #converts the number for each greeting to integer
            number = int(number)
            
            #adds to count
            count += number
    return count


# In[115]:


unread_messages(data)

