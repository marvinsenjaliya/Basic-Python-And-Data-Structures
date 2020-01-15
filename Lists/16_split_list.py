"""
Created on 1/15/2020
@author :Marvin Senjaliya
"""


"""
problem statement:
Write a Python program to split a list based on first character of word.  
"""

list = ["hi","my","name","is","marvin","and","what","is","your","name"]
list2=[]
for word in list:
	f=word[0]
	if word not in list2:
		for i in list:
			if f == i[0]:
				list2.append(i)
print(list2)
