"""
Created on 1/13/2020
@author :Marvin Senjaliya
"""

"""
problem statement:
 Write a Python function to find the maximum and minimum numbers from a sequence of numbers
"""


def min_max(value):
	l=value[0]
	s=value[0]
	for i in value:
		if i>l:
			l=i
		elif i<s:
			s=i
	return l,s
print(min_max([2,1,23,45,56]))
