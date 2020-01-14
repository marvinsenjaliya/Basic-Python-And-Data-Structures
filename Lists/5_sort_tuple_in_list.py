"""
Created on 1/14/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
 Write a Python program to get a list, sorted in increasing order by the last element in each tuple 
from a given list of non-empty tuples.   
	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
 
"""

sample_list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
for x_index in range(len(sample_list)):
	for y_index in range(len(sample_list)):
		if sample_list[x_index][-1]<sample_list[y_index][-1]:
			temp=sample_list[x_index]
			sample_list[x_index]=sample_list[y_index]
			sample_list[y_index]=temp
print(sample_list)
