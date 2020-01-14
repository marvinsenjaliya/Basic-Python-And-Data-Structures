"""
Created on 1/14/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
"""

str='w3resource'
dic={}
for i in str:
	dic[i]=str.count(i)
print(dic)
