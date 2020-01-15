"""
Created on 1/15/2020
@author :Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to find the repeated items of a tuple.
"""

tuple=(1,2,3,3,4,5)
list=list(tuple)
list2=[]
for i in list :
	if i in list2:
		print(i)
	list2.append(i) 


