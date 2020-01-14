"""
Created on 1/14/2020
@author :Marvin Senjaliya
"""

"""
problem statement:
 Write a Python program to print all unique values in a dictionary. 
	Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, 
{"V":"S009"},{"VIII":"S007"}]
	Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""

dic1={}
dic2=[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
unique_value=set(val for i in dic2 for val in i.values())
print(unique_value)
