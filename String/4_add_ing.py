"""
Create on 1/15/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the 
given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is 
less than 3, leave it unchanged.  
	Sample String : 'abc'
	Expected Result : 'abcing' 
	Sample String : 'string'
	Expected Result : 'stringly'
"""

sample_string="abc"
length_string=len(sample_string)
if length_string>1:
	result_string = sample_string+"ing"
if sample_string[-1:-4]=="ing":
	result_string= sample_string+"ly"
print(result_string)
