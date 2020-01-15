"""
Created on 1/15/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a python program to check whether two lists are circularly identical.  
 
"""


def circularly_identical(list1,list2):
	list3=list1*2
	for x in range(0,len(list1)):
		z=0
		for y in range(x,x+len(list2)):
			if list2[z]==list3[y]:
				z=z+1
			else:
				break
		if z==len(list1):
			return True
	return False
list1 = [10, 10, 0, 0, 10] 
list2 = [10, 10, 10, 0, 0] 
list3 = [1, 10, 10, 0, 0] 
if circularly_identical(list1,list2):
	print("yes")
else:
	print("no")
if circularly_identical(list2,list3):
	print("yes")
else:
	print("no")
