"""
Created on 1/15/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
2. Write a Python program to count the number of characters (character frequency) in a string.  
Sample String : google.com
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""

sample_string="google.com"
result={}
for i in sample_string:
	result[i]=sample_string.count(i)
print(result)
