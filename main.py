#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 14:52:49 2021

@author: pierrebourbon
"""

from book import Book

def main(): 
    book = Book("TEST")
    book.insert_Buy(10,10.0)
    book.insert_Sell(120,12.0)
    book.insert_Buy(5, 10.0)
    book.insert_Buy(2,11.0)
    book.insert_Sell(1,10.0)
    book.insert_Sell(10,10.0)
    
if __name__ == "__main__":
    main() 
