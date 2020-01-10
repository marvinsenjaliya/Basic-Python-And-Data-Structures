"""
Created on 1/10/2020
@author: Marvin Senjaliya
"""

"""
problem statement:
 Write a python program which accepts a sequence of comma-separated numbers 
 and generate a list and a tuple with those numbers.
"""

data =input("please enter the numbers")
new_data=data.split(",")
list_data=list(new_data)
print("list_data",list_data)
tuple_data=tuple(new_data)
print("tuple_data",tuple_data) 

