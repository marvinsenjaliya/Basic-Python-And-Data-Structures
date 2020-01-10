"""
Created 1/10/2020
@author:Marvin Senjaliya
"""

""" Problem Statement: Write the program to find the days between two 
dates. """ 
from datetime import date
f_date = date(2014,7,2)
l_date = date(2014,7,11)
delta = l_date-f_date
print(delta.days)
