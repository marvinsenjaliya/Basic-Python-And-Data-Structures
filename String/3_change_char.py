"""
Created on 1/15/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
. Write a Python program to get a string from a given string where all occurrences of its first char 
have been changed to '$', except the first char itself.  
	Sample String : 'restart'
	Expected Result : 'resta$t'

"""


sample_string='restart'
t=sample_string[0]
sample_string=sample_string.replace(t,'$')
sample_string=t+sample_string[1:]
print(sample_string)
