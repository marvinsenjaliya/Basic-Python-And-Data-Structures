""" 
Created on 2/10/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
write a program to concatenate all the elments in a list
into the string 
"""
list = ["hi","my","name","is","marvin"]
output=''
for i in list:
	output+=str(i)+"-"
output=output[:-1]
print(output)

