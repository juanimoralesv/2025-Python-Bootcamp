# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:52:00 2025

@author: JuaniX
"""
# two.py
import UDM_Python_BTCMP__009_04__ONE as one

print("Top level in two.py!")

one.func()

if __name__ == '__main__':
    print("two.py is being run directly!")
else:
    print("two.py has been imported!")