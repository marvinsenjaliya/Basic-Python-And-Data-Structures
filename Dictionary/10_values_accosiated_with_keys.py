XX"""
Created on 1/14/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
 Write a Python program to count the values associated with key in a dictionary. 
	Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 
'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
	Expected result: Count of how many dictionaries have success as True
"""

sample_data=[{'id':1,'success':True,'name':'Lary'},{'id':2,'success':False,'name':'robi'},
{'id':3,'success':True,'name':'Alex'}]
c=0
for i in sample_data:
	print(i)
	if i.get('success')==True:
		c=c+1
		print(c)

