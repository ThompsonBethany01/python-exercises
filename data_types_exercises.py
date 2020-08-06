#!/usr/bin/env python
# coding: utf-8

# # Identify the data type of the following values:
# #### 99.9
# Float 
# #### "False"
# String aka str
# #### False
# Boolean aka bool
# #### '0'
# String aka str
# #### 0
# Int
# #### True
# Boolean aka bool
# #### 'True'
# String
# #### [{}]
# List
# #### {'a': []}
# Dictionary aka dict

# In[11]:


# You can check the data type by using type()
type(False)


# # What data type would best represent:
# 
# #### A term or phrase typed into a search box? 
# A string
# 
# #### If a user is logged in? 
# boolean, is_logged_in = True or False
# 
# #### A discount amount to apply to a user's shopping cart? 
# A float, total * discount, if 20% off it could be 120.93 * 0.20 = discounted amount to subtract from total
# 
# #### Whether or not a coupon code is valid? 
# A boolean, is_valid = True or False
# 
# #### An email address typed into a registration form? 
# A string 'beth@gmail.com'
# 
# #### The price of a product? 
# A float, i.e. 1.99
# 
# #### A Matrix? 
# A Dictionary of lists
#             {col_1: [1,4,5]
#              col_2: [7,8,3]
#              col_3: [1,6,2]}   would be a 3 by 3 matrix
#  
# #### The email addresses collected from a registration form? 
# A dictionary of emails 
# [
# {
#     "name": 'Beth'
#     "email": 'beth@gmail.com'
# },
# {
#     "name": 'Twix'
#     "email": 'twix@gmail.com'
# },
# ]
# 
# #### Information about applicants to Codeup's data science program? 
# A list of dictionaries
# [
#     {
#         "name": "Bethany"
#         "birth_date": "02-05-1997"
#         "program": "data science"
#     },
#     {
#         "name": "Spaghetti"
#         "birth_date": "02-05-1997"
#         "program": "data science"
#     },
#     {
#         "name": "Twix"
#         "birth_date": "02-05-1997"
#         "program": "data science"
#     }
# ]

# # For each of the following code blocks, read the expression and predict what the result of evaluating it would be...

# In[15]:


# results in an error, cannot concat an int
'1' + 2


# In[16]:


#Modulo operator, can divide 6 by 4 once with 2 remainder, outputs 2
6 % 4


# In[17]:


# 6 % 4 = 2, so the type will be an integer
type(6 % 4)


# In[18]:


# The type of int is a data type
type(type(6 % 4))


# In[19]:


# Error - cannot concat an integer
'3 + 4 is ' + 3 + 4


# In[20]:


# The boolean false, 0 is equal to 0 not less than
0 < 0


# In[21]:


# The boolean False, the string "false" is not the same, string != bool
'False' == False


# In[22]:


# The boolean False, the string "false" is not the same, string != bool
True == 'True'


# In[23]:


# True, 5 is greater than OR equal to -5
5 >= -5


# In[31]:


# Using a ! is not correct syntax, though the code by itself does not give an error, it shows and error with type
get_ipython().system('False or False')
type(!False or False)


# In[32]:


# An or statement only needs one value to be True to evaluate as True
True or "42"


# In[33]:


# Again, improper use of ! creates a syntax error
get_ipython().system('True && !False')


# In[34]:


# Because 6/5 has a remainder of 1, the output will be 1
6 % 5


# In[64]:


# False, only one statement needs to be false with 'and'
5 < 4 and 1 == 1


# In[65]:


# False, only one statement needs to be false with 'and', Python is case sensitive
'codeup' == 'codeup' and 'codeup' == 'Codeup'


# In[66]:


#TSyntax error, the correct operand for not equal too is !=
4 >= 0 and 1 !== '1'


# In[67]:


# True, 6/3 has no remainder thus 0 == 0
6 % 3 == 0


# In[68]:


#True, 5/2 has a remainder 1 and 1 does not equal 0
5 % 2 != 0


# In[69]:


# Error, concat function + only adds list wiht list, not int with list
[1] + 2


# In[70]:


# Adds the list together to [1,2]
[1] + [2]


# In[72]:


# Mulitplys the amount of items in list, not actual value
[1] * 2


# In[73]:


# Error, can not multiply non-integers
[1] * [2]


# In[74]:


# You can concat a list, and adding two empty lists is still an empty list
[] + [] == []


# In[75]:


# Error, you can not add dictionaries
{} + {}


# # Write some Python code (variables and operators) to describe the following scenarios. 
# ## Do not worry about the real operations to get the values, the goal of these exercises is to understand how real world conditions can be represented with code.

# # 1.
# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?

# #### Each movie must be a different variable based on the amount of days to be rented.
# - the_little_mermaid = 3
# - brother_bear = 5
# - hercules = 1
# 
# #### You can then add the variables together and multiply by the price to rent per day.
# - price_per_day = 3
# 
# total_price = (the_little_mermaid + brother_bear + hercules) * 3

# # 2.
# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

# #### Create variables for each company pay...
# - google_pay = 400
# - amazon_pay = 380
# - facebook_pay = 350
# 
# #### And for each company hours worked
# - google_hours = 6
# - amazon_hours = 4
# - facebook_hours = 10
# 
# #### Multiply each company pay by their respective hour, then add all together
# total_pay = (google_pay * google_hours) + (amazon_pay * amazon_hours) + (facebook_pay * facebook_hours)

# # 3.
# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

# #### Use boolean values to determine if she can enroll
# - is_not_full
# - is_not_conflict
# 
# #### If both values are True, she can enroll. Otherwise she cannot. Therefore it would be
# Is_enrolled = is_not_full AND is_not_conflict 

# # 4.
# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

# #### Use boolean values to determine if offer applied
# - is_premium_member
# - is_offer_good
# - is_3_items
# 
# #### The operation would be as follows
# is_offer_applied = (is_premium_member OR is_3_items) AND is_offer_good

# # Use the following code to follow the instructions below:

# In[113]:


username = 'codeup'
password = 'notastrongpassword '


# # Create a variable that holds a boolean value for each of the following conditions:
# 
# - the password must be at least 5 characters
# - the username must be no more than 20 characters
# - the password must not be the same as the username
# - bonus neither the username or password can start or end with whitespace1

# In[114]:


is_good_login = (len(password) >= 5) and (len(password) <= 20) and (username.lower() != password.lower()) and (username[0] != ' ') and (password[0] != ' ')


# In[115]:


is_good_login

