"""
Created on 1/14/2020
@author :Marvin Senjaliya
"""

"""
problem statement:
 Write a Python program to find the list of words that are longer than n from a given list of words.  
"""


list=['hhello','how','are','you','people']
n='men'
new_list=[]
for index in list:
	if len(index)>len(n):
		new_list.append(index)
print(new_list)
