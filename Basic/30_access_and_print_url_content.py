"""
Created on 1/13/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to access and print a URL's content to the console
"""

from http.client import HTTPConnection
conn = HTTPConnection("google.com")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)

