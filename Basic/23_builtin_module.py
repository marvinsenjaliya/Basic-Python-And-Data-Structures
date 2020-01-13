"""
Created on 1/13/2020
@author: Marvin Senjaliaya
"""


"""
problem statement:
Write a Python program to find the available built-in modules. 
"""

import sys
import textwrap
module_name=','.join(sorted(sys.builtin_module_name))
print(textwrap.fill(module_name,width=70))
