"""
Created on 1/14/2020
@author :Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to get the smallest number from a list.  
 
"""

list=['abc','xyz','aba','1221']
count=0
str_count=0
for index in list:
	if len(index)>=2:
		count=count+1
		print(count)
	if index[0]==index[-1]:
		str_count=str_count+1
		print(str_count)
