#!/usr/bin/env python
# coding: utf-8

# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[176]:


def is_two(var):
    
    #gives an assertion error if the value entered called through the function is not a string or integer
    assert type(var) == int or type(var) == str, "Invalid input - must be string or integer. Try again."
    
    #conditional is only true if the value called through the function is 2 in int or str form
    if var == 2 or var == '2':
        return True
    else:
        return False


# In[177]:


is_two(2)


# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[178]:


def is_vowel(str_var):
    
    #gives anassertion error if the value called through the function is not a string
    assert type(str_var) == str, "Invalid input for function parameter - must be string. Try again."
    
    #creates a set of vowels to compare with
    vowels = set("aeiouAEIOU")
    
    #conditional is true if the string is in the set vowels
    if str_var in vowels:
        return True
    else:
        return False


# In[190]:


is_vowel('a')


# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[219]:


def is_consonant(char_var):
    
    #gives an assertion error if the value called through the function is not a string
    assert type(char_var) == str, "Invalid input for function parameter - must be string. Try again."
    
    #uses a function that checks vowels to determine if it is a consonant
    #if is_vowel is true, it is not a consonant and therefore False to the outside function
    #if is_vowel is false, it is a consonant and therefore True to the outside function
    if is_vowel(char_var) == True:
        return False
    else:
        return True


# In[221]:


is_consonant('a')


# Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[156]:


def str_cap(word):
    
    #gives an error if the value called through the function is not a string
    assert type(word) == str, "Invalid input for function parameter - must be string. Try again."
    
    #creates a set of vowels to compare with
    vowels = set("aeiou")
    
    #conditional met if the word does not start with a vowel
    if word[0] not in vowels:
        #capitalizes the word
        return word.capitalize()
    else:
        #returns print statement if word starts with vowel, number, etc.
        return print('No capitalization needed.')


# In[166]:


str_cap(123)

str_cap([egg, banana, car])
# In[165]:


str_cap('egg')


# In[164]:


str_cap('bananas')


# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[157]:


def calculate_tip(tip, bill):
    
    #gives an error if values called through function are not decimals
    assert type(tip) == float and type(bill) == float, "Invalid input for function parameters - must be decimals. Try again."
    
    #calculates total tip to give by multiplying tip percent and total bill
    tip_total = tip * bill
    
    #puts the amounts in dollar formatting
    tip_total = "${:,.2f}".format(tip_total)
    print(f"The total tip to give is {tip_total}!")
    return tip_total


# In[159]:


calculate_tip(.2, 25.99)


# Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[259]:


def apply_discount(og_price, disc):
    
    #gives an error if that values passed through the function are not floats
    assert type(og_price) == float and type(disc) == float, "Invalid input for function parameters - must be decimals. Try again."
    
    #amount saved = the total price * the discount
    saving = og_price * disc
    #the new total is the old total - the amount saved
    new_total = og_price - saving
    
    #puts the amounts in dollar formats
    og_price = "${:,.2f}".format(og_price)
    saving = "${:,.2f}".format(saving)
    new_total = "${:,.2f}".format(new_total)
    
    #prints the amounts in a human readable output
    print(f"The original price was {og_price}. Your discount saved you {saving}! You're new price is {new_total}.")
    return new_total


# In[266]:


apply_discount(10.99, .25)


# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[160]:


def handle_commas(num_str):
    
    #gives an error if the value called through the function is not a string
    assert type(num_str) == str, "Invalid input for function parameter - must be string. Try again."
    
    #creates an empty string to add the string values that are not commas
    new_str = ''
    
    #loops through the original string
    for char in num_str:
        #continues the loop if the char is a comma
        if char == ',':
            continue
        #adds to the new string if the char is not a comma
        new_str += char
        
    #converts the value to an integer
    int(new_str)
    return new_str


# In[161]:


handle_commas('234,245,654,676,457')


# Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[275]:


def get_letter_grade(grade):
    
    #gives an error if the value called through the function is not an integer
    assert type(grade) == int, "Invalid input for function parameter - must be integer. Try again."
    
    #gives an output sentence
    print('Your grade is: ')
    
    #conditionals to assign each grade its letter value
    if 100 >= int(grade) >= 90:
        return 'A'
    
    if 89 >= int(grade) >= 80:
        return 'B'

    if 79 >= int(grade) >= 70:
        return 'C'

    if 69 >= int(grade) >= 60:
        return 'D'

    if 59 >= int(grade) >= 0:
        return 'F'


# In[278]:


get_letter_grade(78)


# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[279]:


def remove_vowels(my_str):
    
    #gives an error if the value passed through the function is not a string
    assert type(my_str) == str, "Invalid input for function parameter - must be string. Try again."
    
    #creates a set of vowels to compare with
    vowels = set('aeiouAEIOU')
    
    #creates a new empty string
    new_str = ''
    for char in my_str:
        if char not in vowels:
            new_str += char
    print(new_str)


# In[280]:


remove_vowels('bananas')


# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# - for example:
#     - Name will become name
#     - First Name will become first_name
#     - % Completed will become completed

# In[281]:


def normalize_name(old_str):
    
    #gives an error if the value passed through the function is not a string
    assert type(old_str) == str, "Invalid input for function parameter - must be string. Try again."
    
    #sets empty string to be returned
    new_str = ''
    
    #all nonvalid python characters
    remove = set("!@#$%^&*()+=-[]{}\/|?.<>,`~")
    
    #removes leading and trailing whitespace
    old_str = old_str.strip()
    
    #makes all characters lowercase
    old_str = old_str.lower()
    
    #loops through old_str to check for nonvalid characters and spaces
    for x in old_str:
        #changes spaces to underscore
        if x == ' ':
            new_str += '_'
            continue
        #adds valid characters to new string
        if x not in remove:
            new_str += x
    return new_str


# In[282]:


normalize_name(' @#$FG243 523# $%gNDFJwC# %$T4g ')


# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[182]:


def cumulative_sum(num_list):
    
    #gives error if the value passed through the function is not a list of numbers
    assert type(num_list) == list, "Invalid input for function parameter - must be list. Try again."
    
    #gives error if values inside the list are not integers
    for x in num_list:
        assert type(x) == int, "Invalid input for function parameter - must be list of numbers. Try again."
    
    #creates an empty list to append the cumulative sum inside
    new_list = []
    count = 0
    for x in num_list:
        x += count
        count = x
        new_list.append(x)
    return new_list


# In[183]:


cumulative_sum([1,1,1])
cumulative_sum([1, 2, 'a'])


# # Bonus

# - Create a function named twelveto24. 
# - It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. 
# - Bonus write a function that does the opposite.

# In[300]:


#code not using imports
def twelveto24(time_str):
    assert type(time_str) == str, "Invalid input for function parameter - must be string. Try again."
    new_str = ''
    twelve_stamp = set('ampm')
    
    if time_str[-2] == 'a':
        for x in time_str:
            if x not in twelve_stamp:
                new_str += x
                
    if time_str[-2] == 'p':
        
        for x in time_str:
            if x not in twelve_stamp:
                new_str += x
                
        if len(new_str) == 4:
            new_str = '0' + new_str
            
        old_hour = int(new_str[0:2])
        new_hour = old_hour + 12
        old_hour = str(old_hour)
        new_hour = str(new_hour)
        
        new_str = new_str.replace(old_hour, new_hour)
        
        if len(new_str) == 6:
            new_str = new_str.replace('0', '')
        
    return new_str


# In[303]:


twelveto24('12:45pm')


# - Create a function named col_index. 
# - It should accept a spreadsheet column name, and return the index number of the column.
#     - col_index('A') returns 1
#     - col_index('B') returns 2
#     - col_index('AA') returns 27

# In[116]:


def letter_value(letter):
    count = 1
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for char in letters:
        if char != letter:
            count += 1
        else:
            break
    return count


# In[117]:


letter_value('Z')


# In[400]:


def col_index(col_name):
    total = 0
    count = 0
    for char in col_name:
        col = letter_value(char)
        addition = count * 26
        total = col + addition
        count += 1
    return total


# In[401]:


col_index('AB')


# In[48]:


def col_index(col_name):
    
    if len(col_name) == 1:
        return letter_value(col_name)
    
    total = 0
    if len(col_name) > 1:
        first_letter = col_name[0]
        times = letter_value(first_letter)
        times = times * 26
    
        second_letter = col_name[1]
        col = letter_value(second_letter)
        total = col + times
        
    return total


# In[49]:


col_index('ZZ')


# In[180]:


def col_index(col_name):
    
    #if only one letter, checks the value with function that assigned a value to each individual letter
    if len(col_name) == 1:
        return letter_value(col_name)
    
    #for two letters, the value is 
    total = 0
    if len(col_name) == 2:
        first_letter = col_name[0]
        times = letter_value(first_letter)
        times = times * 26
    
        second_letter = col_name[1]
        col = letter_value(second_letter)
        total = col + times
        
    if len(col_name) == 3:
        first_letter = col_name[0]
        times = letter_value(first_letter)
        times = times * (26 ** 2) 
        total = total + times
        
        second_letter = col_name[1]
        second_times = letter_value(second_letter)
        second_times = second_times * 26
        total = total + second_times
        
        third_letter = col_name[2]
        col = letter_value(third_letter)
        
        total = total + col
        
    return total


# In[181]:


col_index('ZZZ')


# In[ ]:




