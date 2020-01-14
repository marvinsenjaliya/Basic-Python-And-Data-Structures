"""
Created on 1/14/2020
@author:Marvin Senjaliya
"""


"""
problem statement:
Write a Python program to check multiple keys exists in a dictionary. 
"""
#take dictionary as input
dictionary={'ravi':10,'mar':20,'dhaval':30}
#take a empty list
list=[]
#iterate and check using condition wethear multiple key present or not
for key in dictionary.keys():
	if key in list:
		print("yes present")
	list.append(key)
else:
	print("not present")

	

