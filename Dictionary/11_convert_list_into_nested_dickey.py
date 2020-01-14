"""
Created on 1/14/2020
@author :Marvin Senjaliya
"""

"""
problem statement :
Write a Python program to convert a list into a nested dictionary of keys.
"""
list=[1,2,3,4,5]
dict1={}
for i in list:
	dict1[i]={}
	dict1.get(i)[i]={}
print(dict1)

