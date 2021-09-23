#!/usr/bin/env python
# coding: utf-8

# In[30]:


#1.1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
ls = []
for i in range(2000,3200):
    if i % 7 == 0 and i % 5!=0:
        ls.append(i)
print(ls)


# In[31]:


#2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.
a = input("Enter first name:-")
b = input("Enter last name:- ")
c = (" ")
d = a+c+b
print(d[::-1])


# In[27]:


#   3. Write a Python program to find the volume of a sphere with diameter 12 cm.
#   Formula: V=4/3 * π * r 3
d = int(input("Enter diameter of sphere:-"))
r = d /2
pie = 3.14
v = 4/3 * pie * r*r*r
print(v)


# In[ ]:




