"""
Created on 1/15/2020
@author :Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to create the colon of a tuple
"""


from copy import deepcopy
tuplex=("hello",5,[],True)
print(tuplex)
tuplex_colon=deepcopy(tuplex)
tuplex_colon[2].append(50)
print(tuplex_colon)
print(tuplex)
