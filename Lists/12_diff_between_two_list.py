"""
Created on  1/15/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to get the difference between the two lists.  
"""


list1=[1,2,3,4,5,6]
list2=[3,45,67,89,6]
list3=[]
for index in list1:
	if index not in list2:
		list3.append(index)
for index in list2: 
	if index not in list1:
		list3.append(index)
print(list3)


