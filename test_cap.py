# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:36:34 2025

@author: JuaniX

Tests for cap_file.py
"""

import unittest
import cap_file

class TestCapFile(unittest.TestCase):

    def test_one_word(self):
        text = "python"
        result = cap_file.cap_text(text)
        self.assertEqual(result, "Python")

    def test_multiple_words(self):
        text = "monty python"
        result = cap_file.cap_text(text)
        self.assertEqual(result, "Monty Python")

if __name__ == "__main__":
    unittest.main()
    

