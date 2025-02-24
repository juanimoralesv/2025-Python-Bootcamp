# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:45:00 2025

@author: JuaniX
"""
# one.py

def func():
    print("func() in one.py")

print("Top level in one.py!")

if __name__ == '__main__':
    print("one.py is being run directly!")
else:
    print("one.py has been imported!")