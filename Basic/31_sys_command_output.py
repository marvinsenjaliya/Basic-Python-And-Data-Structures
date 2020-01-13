"""
Created on 1/13/2020
@author :Marvin Senjaliya
"""

"""
problem statement :
Write a Python program to get system command output
"""

import subprocess
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
print(returned_text)

