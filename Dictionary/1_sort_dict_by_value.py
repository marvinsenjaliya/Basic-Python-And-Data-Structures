"""
Created on 1/13/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to remove the first occurrence of a specified element from an array. 
"""

def dictionary():
	key_value={}
	key_value[1]='23'
	key_value[2]='34'
	key_value[3]='45'
	key_value[4]='70'
	key_value[5]='300'
	print(sorted(key_value.items(),key=lambda kv:(kv[1],kv[0])))
dictionary()
