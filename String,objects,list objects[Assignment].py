#!/usr/bin/env python
# coding: utf-8

# In[73]:


#1. Create the below pattern using nested for loop in Python.

n = 5 
for i in range(n):
    for j in range(i+1):
           print(end="*")
    print("")
for i in range(n+1,0,-1):
    for j in range(i-2):
        print(end = "*")
    print("")


# In[87]:


#2. Write a Python program to reverse a word after accepting the input from the user.

a = input("Enter a word :-")
print(a[::-1])


# In[ ]:




