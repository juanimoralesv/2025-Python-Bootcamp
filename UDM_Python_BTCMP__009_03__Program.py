# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:40:08 2025

@author: JuaniX
"""
# Using files in root directory
from UDM_Python_BTCMP__009_02__module import my_func
my_func()

# Importing from a package
from MyMainPackage import some_main_script
# Importing from a subpackage
from MyMainPackage.Subpackage import my_subscript

# Run function from package
some_main_script.main_report()
# Run function from subpackage
my_subscript.sub_report()