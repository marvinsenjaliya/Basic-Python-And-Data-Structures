"""
 Created on 1/10/2020
 @author:Marvin Senjaliya
"""


"""
program statement:
write a python program to create a histogram from a given list of integers
"""
def histogram(data):
        for i in data:
		time=i
		output=''
		while(time>0):
			output+='*'
			time=time-1
		print(output)

