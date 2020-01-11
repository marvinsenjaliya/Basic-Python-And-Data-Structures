"""
Created on 02/10/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
write a python program to print out a set containing all the colors from 
color_list_1 are not present in color_list_2.
"""

list_1=["Red","Yellow","White"]
list_2=["Black","pink","Red"]
list_3=[]
list_4=[]
for i in list_1:
	if i in list_2:
		list_3.append(i)
	else:
		list_4.append(i)
print(list_4)

