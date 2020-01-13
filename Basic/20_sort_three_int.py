"""
Created on 1/13/2020
@author :Marvin Senjaliya
"""

"""
problem statement:
 Write a Python program to sort three integers without using conditional statements and loops. 

"""

#take three input
x=int(input("please enter first number:"))
y=int(input("please enter second number:"))
z=int(input("please enter third number:"))
#take min and max number using min and max function
a1=min(x,y,z)
a2=max(x,y,z)
a3=x+y+z-a1-a2
print("three sorted number :"a1,a2,a3)

