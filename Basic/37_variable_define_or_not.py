"""
Created on 1/13/2020
@author :Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to determine if variable is defined or not
"""


try:
  x=1
except NameError:
  print("variable is not define")
else:
  print("variable is define")
try:
  y
except NameError:
  print("variable is not define")
else:
  print("variable is define")

