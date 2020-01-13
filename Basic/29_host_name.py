"""
Created on 1/13/2020
@author :Marvin Senjaliya
"""

"""
problem statement :
 Write a Python program to get the name of the host on which the routine is running
""""

import socket
host_name = socket.gethostname()
print()
print("host_name:",host_name)
print()
