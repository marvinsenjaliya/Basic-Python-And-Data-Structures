"""
Create on 1/14/2020
@author :Marvin Senjaliya
"""


"""
problem statement:
Write a Python program to remove duplicates from a list
"""

list=[1,2,3,4,4,5,3]
list2=[]
for index in list:
	if index not in list2:
		list2.append(index)
print(list2)
