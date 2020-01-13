"""
Created on 1/13/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
 Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
"""

#take input list 
my_list=[120,35,60,90,50,300]
result = list(filter(lambda x: (x % 15 == 0), my_list))
print(result)
