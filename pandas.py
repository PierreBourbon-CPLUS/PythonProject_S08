#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 10:38:52 2021

@author: pierrebourbon
"""

import pandas as pd


class Order: 
    def __init__(self, NbrAction, Price, OrderType):
        self.NbrAction = NbrAction
        self.Price = Price
        self.OrderType = OrderType
        
        
class Book:
    def __init__(self, BookName):
        self.BookName = BookName 
        self.BuyOrders = []
        self.SellOrders = []
       
    def BookState_BuySide(self):
        NbrAction = []
        Price = []
        if self.BuyOrders == []: 
            print("Order book : BUY SIDE \n There are no orders in the book \n")
        else:
            for i in range(len(self.BuyOrders)):
                NbrAction.append(self.BuyOrders[i].NbrAction)
                Price.append(self.BuyOrders[i].Price)       
                
            df = pd.DataFrame({"Nbr Action" : NbrAction, "Price" : Price})
            print("Order book : BUY SIDE" '\n', df,'\n')

            
    def BookState_SellSide(self):
        NbrAction = []
        Price = []
        if self.SellOrders == []:
            print("Order book : SELL SIDE \n There are no orders in the book \n")
        else:
            for i in range(len(self.SellOrders)):
                NbrAction.append(self.SellOrders[i].NbrAction)
                Price.append(self.SellOrders[i].Price)       
                
            df = pd.DataFrame({"Nbr Action" : NbrAction, "Price" : Price})
            print("Order book : SELL SIDE" '\n', df,'\n')

    def display_log(self):
        print("This is the log for the order book of",self.BookName, ':\n')
        self.BookState_BuySide()
        self.BookState_SellSide()
        

    def insert_Buy(self, NbrAction, Price):
        order = Order(NbrAction, Price, 'Buy')
        print ("Insert Buy Order",order.NbrAction,"@", order.Price, "in",self.BookName)        
        if self.BuyOrders == []:
            self.BuyOrders.append(order)
            print("First order in the book \n")
        else:
            for i in range(len(self.BuyOrders)):
                if self.BuyOrders[i].Price < order.Price:
                    self.BuyOrders.insert(i,order)
                    print( "Order added to the book \n")
                    break
                elif self.BuyOrders[i].Price == order.Price:
                    if len(self.BuyOrders)<=i+1:
                        self.BuyOrders.append(order)
                        print("Order added after a similar order \n")
                        break
                    elif self.BuyOrders[i+1].Price < order.Price:
                        self.BuyOrders.insert(i+1,order)
                        print("Order added after a similar order \n")
                        break
            if self.BuyOrders[-1].Price > order.Price:
                self.BuyOrders.append(order)
                print("Order added at the end of the queue \n")
        self.trade_activation()


    def insert_Sell(self, NbrAction, Price):
        order = Order(NbrAction, Price, 'Sell')
        print ("Insert Sell Order",order.NbrAction,"@", order.Price, "in",self.BookName)
        if self.SellOrders == []:
            self.SellOrders.append(order)
            print("First order in the book \n")
        else:
            for i in range(len(self.SellOrders)):
                if self.SellOrders[i].Price > order.Price:
                    self.SellOrders.insert(i,order)
                    print( "Order added to the book \n")
                    break
                elif self.SellOrders[i].Price == order.Price:
                    if len(self.SellOrders)<=i+1:
                        self.SellOrders.append(order)
                        print("Order added after a similar order \n")
                        break
                    elif self.SellOrders[i+1].Price > order.Price:
                        self.SellOrders.insert(i+1,order)
                        print("Order added after a similar order \n")
                        break
            if self.SellOrders[-1].Price < order.Price:
                self.SellOrders.append(order)
                print("Order added at the end of the queue \n")
        self.trade_activation()
              
        
    def trade_activation(self):
        while self.BuyOrders != [] and self.SellOrders != []:
            BidAskSpread = self.BuyOrders[0].Price - self.SellOrders[0].Price
            if BidAskSpread <0:
                break
            else:
                if self.BuyOrders[0].Price >= self.SellOrders[0].Price:
                    TradePrice = min(self.SellOrders[0].Price, self.BuyOrders[0].Price)
                    if self.BuyOrders[0].NbrAction == self.SellOrders[0].NbrAction:
                        QuantityTraded = self.BuyOrders[0].NbrAction
                        self.BuyOrders.pop(0)
                        self.SellOrders.pop(0)
                        print("TRADE ACTIVATED : \n Sold",QuantityTraded, "@", TradePrice, '\n')
                    elif self.BuyOrders[0].NbrAction < self.SellOrders[0].NbrAction:
                        QuantityTraded = self.BuyOrders[0].NbrAction
                        self.BuyOrders.pop(0)
                        self.SellOrders[0].NbrAction = self.SellOrders[0].NbrAction - QuantityTraded
                        print("TRADE ACTIVATED : \n Sold",QuantityTraded, "@", TradePrice, '\n')
                    elif self.BuyOrders[0].NbrAction > self.SellOrders[0].NbrAction:
                        QuantityTraded = self.SellOrders[0].NbrAction
                        self.SellOrders.pop(0)
                        self.BuyOrders[0].NbrAction = self.BuyOrders[0].NbrAction - QuantityTraded
                        print("TRADE ACTIVATED : \n Sold",QuantityTraded, "@", TradePrice, '\n')
        self.display_log()  
      


book = Book('TEST')
book.insert_Buy(10,10.0)
book.insert_Buy(1,10.0)
book.insert_Buy(160,15.0)
book.insert_Sell(120,12.0)
book.insert_Buy(5, 10.0)
book.insert_Buy(2,11.0)
book.insert_Sell(110,10.0)
book.insert_Sell(10,10.0)


