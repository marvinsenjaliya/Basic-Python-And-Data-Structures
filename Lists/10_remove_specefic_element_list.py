"""
Created on 1/15/2020
@author:Marvin Senjalia
"""


"""
problem statment:
Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.  
	Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
	Expected Output : ['Green', 'White', 'Black']
 	
"""
sample_list=['red','green','yellow','blue','white']
Expected_output=[]
#remove 0th 4th and 5th position
for index in range(len(sample_list)):
	if index!=0 and index!=3 and index!=4:
		Expected_output.append(sample_list[index])
print(Expected_output)
