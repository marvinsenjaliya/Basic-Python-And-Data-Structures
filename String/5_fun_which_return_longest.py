"""
Created on :1/15/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
. Write a Python function that takes a list of words and returns the length of the longest one.  
"""


def function(list):
	max=0
	for i in list:
		if len(i)>max:
			max=len(i)
	return max
list=["hi","is","this","program","working"]
print(function(list))

