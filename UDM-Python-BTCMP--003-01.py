# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:25:50 2025

@author: JuaniX
"""

# 12 - Python Numbers
print(2 + 1)
print(2 - 1)
print(2 * 2)
print(3 / 2)

# Modulo or Mod operator
print(3 % 4, 'is the remainder of 3 / 4')
print("Useful to check if a number is divisible by another, or if it's even or not.")
print(23 % 2)
print("Hence, odd.")
print(20 % 2)
print("Hence, even.")

# Powers
print(2 ** 3)

# 'Complex' operations
print('2 + 10 * 10 + 3 =', 2 + 10 * 10 + 3)

print('(2 + 10) * (10 + 3) =', (2 + 10) * (10 + 3))

# XX - Exercise
# Expression that results in 100
print('((12 ** 2 - 12 * 4 + 5) % 2 + 299) / 3 =', ((12 ** 2 - 12 * 4 + 5) % 2 + 299) / 3)

# 13 - FAQ Numbers
print('0.1 + 0.2 - 0.3 =', 0.1 + 0.2 - 0.3)

# 14 - Variable Assignment
a = 5
a

a = 10
a

a + a

a = a + a
a

# Check data type
type(a)

a = 30.1
type(a)

int = 4 # See that int is highlighted, because it's a keyword.

# Operations using variables
my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
my_taxes

# 15 - Strings
'hello'+" world"

"I'm going on a run."

# Printing, so the quotes aren't included
print("Hello!")

# Only the last string is shown
"Hello, world one!"
"Hello, world two!"

# Using print shows both
print("Hello, world one!")
print("Hello, world two!")

# Escape sequences
print("Hello, \n world!") # \n -> new line

# Escape sequences
print("Hello, \nworld!") # \n -> new line

# Escape sequences
print("Hello, \t world!") # \t -> tab

# length function
len("Hello, world!")


# 16 - Indexing and Slicing with Strings
mystring = "Hello, world!"
mystring

# Grab a character, indexing
mystring[0]

# Backward indexing
mystring[-2]

# Magic slicing
mystring[::-1]

mystring = "abcdefghijk"
mystring

# string_variable[start : stop : step]
mystring[2:]

mystring[:2]

mystring[2:5]

mystring[::2]