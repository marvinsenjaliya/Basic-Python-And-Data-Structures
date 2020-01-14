"""
Created on 1/14/2020
@author:Marvin Senjaliya
"""


"""
problem statement:
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in 
the form (x, x*x). 
	Sample Dictionary ( n = 5) : 
	Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

dic={} 
n=int(input("Enter the number"))
for x in range(n):
	dic[x]=x*x
print(dic)
