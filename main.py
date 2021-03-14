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
        for i in range(max(len(self.BuyOrders),len(self.SellOrders))):
            if self.BuyOrders != [] and self.SellOrders != []:
                BidAskSpread = self.BuyOrders[0].Price - self.SellOrders[0].Price
                while BidAskSpread > 0:
                    if self.BuyOrders[0].Price == self.SellOrders[0].Price:
                        TradePrice = self.SellOrders[0].Price
                        if self.BuyOrders[0].NbrAction == self.SellOrders[0].NbrAction:
                            QuantityTraded = self.BuyOrders[0].NbrAction
                            self.BuyOrders.pop(0)
                            self.SellOrders.pop(0)
                            print("Trade Activated : \n Sold",QuantityTraded, "@", TradePrice)
                        elif self.BuyOrders[0].NbrAction < self.SellOrders[0].NbrAction:
                            QuantityTraded = self.BuyOrders[0].NbrAction
                            self.BuyOrders.pop(0)
                            self.SellOrders[0].NbrAction = self.SellOrders[0].NbrAction - QuantityTraded
                            print("Trade Activated : \n Sold",QuantityTraded, "@", TradePrice)
                        elif self.BuyOrders[0].NbrAction > self.SellOrders[0].NbrAction:
                            QuantityTraded = self.SellOrders[0].NbrAction
                            self.SellOrders.pop(0)
                            self.BuyOrders[0].NbrAction = self.BuyOrders[0].NbrAction - QuantityTraded
                            print("Trade Activated : \n Sold",QuantityTraded, "@", TradePrice)
                    elif self.BuyOrders[0].Price >= self.SellOrders[0].Price:
                        QuantityTraded = max(self.BuyOrders[0].NbrAction, self.SellOrders[0].NbrAction)
                        for j in range(QuantityTraded):
                            self.BuyOrders[0].NbrAction = self.BuyOrders[0].NbrAction - QuantityTraded
                            if self.BuyOrders[0].NbrAction == 0:
                                self.display_log()  