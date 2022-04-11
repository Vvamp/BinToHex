'''
    File name: sysout.py
    Description: Create a dummy sysout
    Author: Vincent van Setten
    Date created: 23/02/2022
    Date last modified: 11/04/2022
    Python Version: 3.10.2
    License: LICENSE.md
'''

class sysout:
    def __init__(self):
        self.body = ""
        pass 

    def write(self, text_to_write):
        self.body += text_to_write 
    
    def close(self):
        return self.body
