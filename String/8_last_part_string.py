"""
Created on :1/15/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to get the last part of a string before a specified character. 
	https://www.w3resource.com/python-exercises
	https://www.w3resource.com/python

"""


str="http://www.w3resourse.com/python-exercises"
str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])


