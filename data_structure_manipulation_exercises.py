#!/usr/bin/env python
# coding: utf-8

# # The following questions reference the students data structure below. Write the python code to answer the following questions:

# 1. How many students are there?

# In[4]:


#shows length of dictionary, aka 14 items
len(students)


# 2. How many students prefer light coffee? For each type of coffee roast?

# In[8]:


# options are light, medium, dark

#create an empty dictionary with coffee options to add to later
coffee_preference = {'light': '', 'medium': '', 'dark': ''}

#sets the variables for each option
light = 0
medium = 0
dark = 0

#counts how many light
for student in students:
    if student['coffee_preference'] == 'light':
        light += 3
#sets this variable to the dictionary
coffee_preference['light'] = light

#counts how many medium
for student in students:
    if student['coffee_preference'] == 'medium':
        medium += 1
#sets this variable to the dictionary
coffee_preference['medium'] = medium

#counts how many dark
for student in students:
    if student['coffee_preference'] == 'dark':
        dark += 1
#sets this variable to the dictionary
coffee_preference['dark'] = dark

max(coffee_preference[])
 


# 3. How many types of each pet are there?

# In[113]:


#create an empty variable to hold unique pet names
distinct_pets = []

#nested for loop to find species name
for student in students:
    for items in student['pets']:
        #adds species name to list if not already in it
        if items['species'] not in distinct_pets:
            distinct_pets.append(items['species'])

print(distinct_pets)
print(len(distinct_pets))


# 4. How many grades does each student have? Do they all have the same number of grades?

# In[91]:


#create empty list to add grade count of each student
grade_count = []

#sets an empty count variable
count = 0

#checks the length of each students grade list and adds to grade_count
for student in students:
    count = len(student['grades'])
    grade_count.append(count)    
        
grade_count
#output shows all students have 4 grades


# 5. What is each student's grade average?

# In[112]:


#create empty list to add grade average of each student
grade_avg = []

#checks the amount of grades per student
total = 0
count = 0
for student in students:
    count = len(student['grades'])
    total = sum(student['grades'])
    average = total/count
    
    grade_avg.append(average)
       
print(student_avg)


grade_avg


# 6. How many pets does each student have?

# In[ ]:


pet_count = []

count = 0
for student in students:
    count = len(student['grades'])
    total = sum(student['grades'])
    average = total/count
    
    grade_avg.append(average)


# 7. How many students are in web development? data science?

# In[ ]:





# 8. What is the average number of pets for students in web development?

# In[ ]:





# 9. What is the average pet age for students in data science?

# In[ ]:





# 10. What is most frequent coffee preference for data science students?

# In[ ]:





# 11. What is the least frequent coffee preference for web development students?

# In[ ]:





# 12. What is the average grade for students with at least 2 pets?

# In[ ]:





# 13. How many students have 3 pets?

# In[ ]:





# 14. What is the average grade for students with 0 pets?

# In[ ]:





# 15. What is the average grade for web development students? data science students?

# In[ ]:





# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?

# In[ ]:





# 17. What is the average number of pets for medium coffee drinkers?

# In[ ]:





# 18. What is the most common type of pet for web development students?

# In[ ]:





# 19. What is the average name length?

# In[ ]:





# 20. What is the highest pet age for light coffee drinkers?

# In[ ]:





# In[2]:


students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]

