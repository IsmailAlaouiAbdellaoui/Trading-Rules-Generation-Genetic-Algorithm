# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:57:37 2017

@author: Alaoui
"""

import random
#import backtrader as bt
import os
import datetime 
import sys

count = 0
first_rule = []
rule = []
member = []
indicator_list = []
options_list = []
comp_list = []
log_op_list = []
values_list = []

variable_name = []
rulem = []
indicator_listm = []
options_listm = []
comp_listm = []
log_op_listm = []
values_listm = []


mut_rate = 0.05
SMA_range_options = [10,30,50,70,90,110,130]
SMA_range_values = ['SMA(10)','SMA(30)','SMA(50)','SMA(70)','SMA(90)','SMA(110)','SMA(130)','self.dataopen[-1]','self.datahigh[-1]','self.datalow[-1]','self.dataclose[-1]']

#    SMA_value = SMA_range_values[random.randint(0,4)]
#        if SMA_value == 0:
#            SMA_value = SMA_range_options[random.randint(0,6)]

MACD_range_options_EMA_fast = [5,15]
MACD_range_options_EMA_slow = [20,30]
MACD_range_options_SMA = [5,25]
MACD_range_values = 0

RSI_range_options = [10,20,30,40,50]
RSI_range_values = random.randint(0,100)


Momentum_range_options = random.randint(10,20)
Momentum_range_values = round(random.uniform(92.48,109.81),2)



#class TestStrategy(bt.Strategy):
#
#    def __init__(self):
#        # Keep a reference to the "close" line in the data[0] dataseries
#        self.dataclose = self.datas[0].close
#        self.dataopen = self.datas[0].open
#        self.datahigh = self.datas[0].high
#        self.datalow = self.datas[0].low
#        

        
def create_rule():
#    rule = []
    global rule
    global indicator_list
    global options_list
    global comp_list
    global log_op_list
    global values_list
    
    global rulem
    global indicator_listm
    global options_listm
    global comp_listm
    global log_op_listm
    global values_listm
    
    
   
    list_indicators = [0,1,2,3]# 0=> SMA , 1=> MACD, 2=>RSI, 3=>Momentum
    list_comparators = [0,1,2,3,4,5]# 0<, 1<=, 2>, 3>=, 4==, 5!=
    list_logical = [0,1] # 0 and, 1 or
    list_orders = [0,1]# 0 => sell, 1 => buy
    
    SMA_range_options = [10,30,50,70,90,110,130]
    SMA_range_values = ['SMA(10)','SMA(30)','SMA(50)','SMA(70)','SMA(90)','SMA(110)','SMA(130)','self.dataopen[-1]','self.datahigh[-1]','self.datalow[-1]','self.dataclose[-1]']
    
#    SMA_value = SMA_range_values[random.randint(0,4)]
#        if SMA_value == 0:
#            SMA_value = SMA_range_options[random.randint(0,6)]
    
    MACD_range_options_EMA_fast = [5,15]
    MACD_range_options_EMA_slow = [20,30]
    MACD_range_options_SMA = [5,25]
    MACD_range_values = 0
    
    RSI_range_options = [10,20,30,40,50]
    RSI_range_values = random.randint(0,100)
    

    Momentum_range_options = random.randint(10,20)
    Momentum_range_values = round(random.uniform(92.48,109.81),2)

    
    
#    number_indicators = random.randint(2,4)

    number_indicators = 2
    rule.append(number_indicators)
    rulem.append(number_indicators)

### BEGINNING PART WHERE THE NUMBER OF INDICATORS EQUALS  2   ###

    if number_indicators == 2:
        first_indicator = list_indicators[random.randint(0,3)]
        rule.append(first_indicator)
        rulem.append(first_indicator)
        second_indicator = random.randint(0,3)
        rule.append(second_indicator)
        rulem.append(second_indicator)

        
        if first_indicator == 0: #SMA choice
            indicator_list.append('SMA')
            indicator_listm.append('SMA')
            SMA_option_first_indicator = SMA_range_options[random.randint(0,6)]
            rule.append(SMA_option_first_indicator)
            rulem.append(SMA_option_first_indicator)
            options_list.append(SMA_option_first_indicator)
            options_listm.append(SMA_option_first_indicator)
            SMA_value_first_indicator = SMA_range_values[random.randint(0,10)]
            rule.append(SMA_value_first_indicator)
            rulem.append(SMA_value_first_indicator)
            values_list.append(SMA_value_first_indicator)
            values_listm.append(SMA_value_first_indicator)
            #SMA values to be determined , see backtrader so choose OHLC value of last bar
            
        if first_indicator == 1: #MACD choice
            indicator_list.append('MACD')
            indicator_listm.append('MACD')
            MACD_EMA_fast_option_first_indicator = MACD_range_options_EMA_fast[random.randint(0,1)]
            MACD_EMA_slow_option_first_indicator = MACD_range_options_EMA_slow[random.randint(0,1)]
            rule.append(MACD_EMA_slow_option_first_indicator)
            rulem.append(MACD_EMA_slow_option_first_indicator)
            rule.append(MACD_EMA_fast_option_first_indicator)
            rulem.append(MACD_EMA_fast_option_first_indicator)
            
            MACD_SMA_option_first_indicator = MACD_range_options_SMA[random.randint(0,1)]
            rule.append(MACD_SMA_option_first_indicator)
            rulem.append(MACD_SMA_option_first_indicator)
            options_list.append(MACD_EMA_slow_option_first_indicator)
            options_list.append(MACD_EMA_fast_option_first_indicator)
            options_list.append(MACD_SMA_option_first_indicator)
            options_listm.append(MACD_EMA_slow_option_first_indicator)
            options_listm.append(MACD_EMA_fast_option_first_indicator)
            options_listm.append(MACD_SMA_option_first_indicator)
            MACD_value_first_indicator = MACD_range_values
            rule.append(MACD_value_first_indicator)
            rulem.append(MACD_value_first_indicator)
            values_list.append(MACD_value_first_indicator)
            values_listm.append(MACD_value_first_indicator)
            
        if first_indicator == 2: #RSI choice
            indicator_list.append('RSI')
            indicator_listm.append('RSI')
            RSI_option_first_indicator = RSI_range_options[random.randint(0,4)]
            options_list.append(RSI_option_first_indicator)
            rule.append(RSI_option_first_indicator)
            options_listm.append(RSI_option_first_indicator)
            rulem.append(RSI_option_first_indicator)
            RSI_value_first_indicator = RSI_range_values
            rule.append(RSI_value_first_indicator)
            values_list.append(RSI_value_first_indicator)
            rulem.append(RSI_value_first_indicator)
            values_listm.append(RSI_value_first_indicator)
            
        if first_indicator == 3: #Momentum choice
            indicator_list.append('Momentum')
            indicator_listm.append('Momentum')
            Momentum_option_first_indicator = Momentum_range_options
            options_list.append(Momentum_range_options)
            rule.append(Momentum_option_first_indicator)
            options_listm.append(Momentum_range_options)
            rulem.append(Momentum_option_first_indicator)
            Momentum_value_first_indicator = round(random.uniform(92.48,109.81),2)
            rule.append(Momentum_value_first_indicator)
            values_list.append(Momentum_value_first_indicator)
            rulem.append(Momentum_value_first_indicator)
            values_listm.append(Momentum_value_first_indicator)
            
         #SECOND INDICATOR PART   
            
        if second_indicator == 0: #SMA choice
            indicator_list.append('SMA')
            indicator_listm.append('SMA')
            SMA_option_second_indicator = SMA_range_options[random.randint(0,6)]
            options_list.append(SMA_option_second_indicator)
            rule.append(SMA_option_second_indicator)
            options_listm.append(SMA_option_second_indicator)
            rulem.append(SMA_option_second_indicator)
            SMA_value_second_indicator = SMA_range_values[random.randint(0,10)]
            rule.append(SMA_value_second_indicator)
            values_list.append(SMA_value_second_indicator)
            rulem.append(SMA_value_second_indicator)
            values_listm.append(SMA_value_second_indicator)
            #SMA values to be determined , see backtrader so choose OHLC value of last bar
            
        if second_indicator == 1: #MACD choice
            indicator_list.append('MACD')
            indicator_listm.append('MACD')
            MACD_EMA_fast_option_second_indicator = MACD_range_options_EMA_fast[random.randint(0,1)]
            MACD_EMA_slow_option_second_indicator = MACD_range_options_EMA_slow[random.randint(0,1)]
            rule.append(MACD_EMA_slow_option_second_indicator)
            rule.append(MACD_EMA_fast_option_second_indicator)
            rulem.append(MACD_EMA_slow_option_second_indicator)
            rulem.append(MACD_EMA_fast_option_second_indicator)
            MACD_SMA_option_second_indicator = MACD_range_options_SMA[random.randint(0,1)]
            rule.append(MACD_SMA_option_second_indicator)
            options_list.append(MACD_EMA_slow_option_second_indicator)
            options_list.append(MACD_EMA_fast_option_second_indicator)
            options_list.append(MACD_SMA_option_second_indicator)
            rulem.append(MACD_SMA_option_second_indicator)
            options_listm.append(MACD_EMA_slow_option_second_indicator)
            options_listm.append(MACD_EMA_fast_option_second_indicator)
            options_listm.append(MACD_SMA_option_second_indicator)
            MACD_value_second_indicator = MACD_range_values
            rule.append(MACD_value_second_indicator)
            values_list.append(MACD_value_second_indicator)
            rulem.append(MACD_value_second_indicator)
            values_listm.append(MACD_value_second_indicator)
            
        if second_indicator == 2: #RSI choice
            indicator_list.append('RSI')
            indicator_listm.append('RSI')
            RSI_option_second_indicator = RSI_range_options[random.randint(0,4)]
            rule.append(RSI_option_second_indicator)
            options_list.append(RSI_option_second_indicator)
            rulem.append(RSI_option_second_indicator)
            options_listm.append(RSI_option_second_indicator)
            RSI_value_second_indicator = RSI_range_values
            rule.append(RSI_value_second_indicator)
            values_list.append(RSI_value_second_indicator)
            rulem.append(RSI_value_second_indicator)
            values_listm.append(RSI_value_second_indicator)
            
        if second_indicator == 3: #Momentum choice
            indicator_list.append('Momentum')
            indicator_listm.append('Momentum')
            Momentum_option_second_indicator = Momentum_range_options
            rule.append(Momentum_option_second_indicator)
            options_list.append(Momentum_option_second_indicator)
            rulem.append(Momentum_option_second_indicator)
            options_listm.append(Momentum_option_second_indicator)
            Momentum_value_second_indicator = round(random.uniform(92.48,109.81),2)
            rule.append(Momentum_value_second_indicator)
            values_list.append(Momentum_value_second_indicator)
            rulem.append(Momentum_value_second_indicator)
            values_listm.append(Momentum_value_second_indicator)
            
        first_comparator = list_comparators[random.randint(0,5)]
        rule.append(first_comparator)
        rulem.append(first_comparator)
        comp_list.append(first_comparator)
        comp_listm.append(first_comparator)
        second_comparator = list_comparators[random.randint(0,5)]
        rule.append(second_comparator)
        comp_list.append(second_comparator)
        rulem.append(second_comparator)
        comp_listm.append(second_comparator)
        
        logical_operator = list_logical[random.randint(0,1)]   
        rule.append(logical_operator)
        log_op_list.append(logical_operator)
        rulem.append(logical_operator)
        log_op_listm.append(logical_operator)
        
        order = list_orders[random.randint(0,1)]
        rule.append(order)
        rulem.append(order)
        
        #i = 0
        #while(i<11):
            
         #   i = i + 1
        
        ### BEGINNING PART WHERE THE NUMBER OF INDICATORS EQUALS  3   ###
        
    if number_indicators == 3:
        first_indicator = random.randint(0,3)
        rule.append(first_indicator)
        rulem.append(first_indicator)
        second_indicator = random.randint(0,3)
        rule.append(second_indicator)
        rulem.append(second_indicator)
        third_indicator = random.randint(0,3)
        rule.append(third_indicator)
        rulem.append(third_indicator)
        
        if first_indicator == 0: #SMA choice
            indicator_list.append('SMA')
            indicator_listm.append('SMA')
            SMA_option_first_indicator = SMA_range_options[random.randint(0,6)]
            rule.append(SMA_option_first_indicator)
            options_list.append(SMA_option_first_indicator)
            rulem.append(SMA_option_first_indicator)
            options_listm.append(SMA_option_first_indicator)
            SMA_value_first_indicator = SMA_range_values[random.randint(0,10)]
            rule.append(SMA_value_first_indicator)
            values_list.append(SMA_value_first_indicator)
            rulem.append(SMA_value_first_indicator)
            values_listm.append(SMA_value_first_indicator)
            #SMA values to be determined , see backtrader so choose OHLC value of last bar
                
        if first_indicator == 1: #MACD choice
            indicator_list.append('MACD')
            indicator_listm.append('MACD')
            MACD_EMA_fast_option_first_indicator = MACD_range_options_EMA_fast[random.randint(0,1)]
            MACD_EMA_slow_option_first_indicator = MACD_range_options_EMA_slow[random.randint(0,1)]
            rule.append(MACD_EMA_slow_option_first_indicator)
            rule.append(MACD_EMA_fast_option_first_indicator)
            rulem.append(MACD_EMA_slow_option_first_indicator)
            rulem.append(MACD_EMA_fast_option_first_indicator)
            MACD_SMA_option_first_indicator = MACD_range_options_SMA[random.randint(0,1)]
            rule.append(MACD_SMA_option_first_indicator)
            rulem.append(MACD_SMA_option_first_indicator)
            MACD_value_first_indicator = MACD_range_values
            rule.append(MACD_value_first_indicator)
            options_list.append(MACD_EMA_slow_option_first_indicator)
            options_list.append(MACD_EMA_fast_option_first_indicator)
            options_list.append(MACD_SMA_option_first_indicator)
            values_list.append(MACD_value_first_indicator)
            options_listm.append(MACD_EMA_slow_option_first_indicator)
            options_listm.append(MACD_EMA_fast_option_first_indicator)
            options_listm.append(MACD_SMA_option_first_indicator)
            values_listm.append(MACD_value_first_indicator)
                
        if first_indicator == 2: #RSI choice
            indicator_list.append('RSI')
            indicator_listm.append('RSI')
            RSI_option_first_indicator = RSI_range_options[random.randint(0,4)]
            rule.append(RSI_option_first_indicator)
            options_list.append(RSI_option_first_indicator)
            rulem.append(RSI_option_first_indicator)
            options_listm.append(RSI_option_first_indicator)
            RSI_value_first_indicator = RSI_range_values
            rule.append(RSI_value_first_indicator)
            values_list.append(RSI_value_first_indicator)
            rulem.append(RSI_value_first_indicator)
            values_listm.append(RSI_value_first_indicator)
                
        if first_indicator == 3: #Momentum choice
            indicator_list.append('Momentum')
            indicator_listm.append('Momentum')
            Momentum_option_first_indicator = Momentum_range_options
            rule.append(Momentum_option_first_indicator)
            options_list.append(Momentum_range_options)
            rulem.append(Momentum_option_first_indicator)
            options_listm.append(Momentum_range_options)
            Momentum_value_first_indicator = round(random.uniform(92.48,109.81),2)
            rule.append(Momentum_value_first_indicator)
            values_list.append(Momentum_value_first_indicator)
            rulem.append(Momentum_value_first_indicator)
            values_listm.append(Momentum_value_first_indicator)
                
             #SECOND INDICATOR PART   
                
        if second_indicator == 0: #SMA choice
            indicator_list.append('SMA')
            indicator_listm.append('SMA')
            SMA_option_second_indicator = SMA_range_options[random.randint(0,6)]
            rule.append(SMA_option_second_indicator)
            options_list.append(SMA_option_second_indicator)
            rulem.append(SMA_option_second_indicator)
            options_listm.append(SMA_option_second_indicator)
            SMA_value_second_indicator = SMA_range_values[random.randint(0,10)]
            rule.append(SMA_value_second_indicator)
            values_list.append(SMA_value_second_indicator)
            rulem.append(SMA_value_second_indicator)
            values_listm.append(SMA_value_second_indicator)
            #SMA values to be determined , see backtrader so choose OHLC value of last bar
                
        if second_indicator == 1: #MACD choice
            indicator_list.append('MACD')
            indicator_listm.append('MACD')
            MACD_EMA_fast_option_second_indicator = MACD_range_options_EMA_fast[random.randint(0,1)]
            MACD_EMA_slow_option_second_indicator = MACD_range_options_EMA_slow[random.randint(0,1)]
            rule.append(MACD_EMA_slow_option_second_indicator)
            rule.append(MACD_EMA_fast_option_second_indicator)
            rulem.append(MACD_EMA_slow_option_second_indicator)
            rulem.append(MACD_EMA_fast_option_second_indicator)
            MACD_SMA_option_second_indicator = MACD_range_options_SMA[random.randint(0,1)]
            rule.append(MACD_SMA_option_second_indicator)
            rulem.append(MACD_SMA_option_second_indicator)
            MACD_value_second_indicator = MACD_range_values
            rule.append(MACD_value_second_indicator)
            options_list.append(MACD_EMA_slow_option_second_indicator)
            options_list.append(MACD_EMA_fast_option_second_indicator)
            options_list.append(MACD_SMA_option_second_indicator)
            values_list.append(MACD_value_second_indicator)
            rulem.append(MACD_value_second_indicator)
            options_listm.append(MACD_EMA_slow_option_second_indicator)
            options_listm.append(MACD_EMA_fast_option_second_indicator)
            options_listm.append(MACD_SMA_option_second_indicator)
            values_listm.append(MACD_value_second_indicator)
                
        if second_indicator == 2: #RSI choice
            indicator_list.append('RSI')
            indicator_listm.append('RSI')
            RSI_option_second_indicator = RSI_range_options[random.randint(0,4)]
            rule.append(RSI_option_second_indicator)
            options_list.append(RSI_option_second_indicator)
            rulem.append(RSI_option_second_indicator)
            options_listm.append(RSI_option_second_indicator)
            RSI_value_second_indicator = RSI_range_values
            rule.append(RSI_value_second_indicator)
            values_list.append(RSI_value_second_indicator)
            rulem.append(RSI_value_second_indicator)
            values_listm.append(RSI_value_second_indicator)
                
        if second_indicator == 3: #Momentum choice
            indicator_list.append('Momentum')
            indicator_listm.append('Momentum')
            Momentum_option_second_indicator = Momentum_range_options
            rule.append(Momentum_option_second_indicator)
            options_list.append(Momentum_option_second_indicator)
            rulem.append(Momentum_option_second_indicator)
            options_listm.append(Momentum_option_second_indicator)
            Momentum_value_second_indicator = round(random.uniform(92.48,109.81),2)
            rule.append(Momentum_value_second_indicator)
            values_list.append(Momentum_value_second_indicator)
            rulem.append(Momentum_value_second_indicator)
            values_listm.append(Momentum_value_second_indicator)
            
                
                #3rd indicator part#
                
        if third_indicator == 0: #SMA choice
            indicator_list.append('SMA')
            indicator_listm.append('SMA')
            SMA_option_third_indicator = SMA_range_options[random.randint(0,6)]
            rule.append(SMA_option_third_indicator)
            options_list.append(SMA_option_third_indicator)
            rulem.append(SMA_option_third_indicator)
            options_listm.append(SMA_option_third_indicator)
            SMA_value_third_indicator = SMA_range_values[random.randint(0,10)]
            rule.append(SMA_value_third_indicator)
            values_list.append(SMA_value_third_indicator)
            rulem.append(SMA_value_third_indicator)
            values_listm.append(SMA_value_third_indicator)
            #SMA values to be determined , see backtrader so choose OHLC value of last bar
                
        if third_indicator == 1: #MACD choice
            indicator_list.append('MACD')
            indicator_listm.append('MACD')
            MACD_EMA_fast_option_third_indicator = MACD_range_options_EMA_fast[random.randint(0,1)]
            MACD_EMA_slow_option_third_indicator = MACD_range_options_EMA_slow[random.randint(0,1)]
            rule.append(MACD_EMA_slow_option_third_indicator)
            rule.append(MACD_EMA_fast_option_third_indicator)
            rulem.append(MACD_EMA_slow_option_third_indicator)
            rulem.append(MACD_EMA_fast_option_third_indicator)
            MACD_SMA_option_third_indicator = MACD_range_options_SMA[random.randint(0,1)]
            rule.append(MACD_SMA_option_third_indicator)
            rulem.append(MACD_SMA_option_third_indicator)
            MACD_value_third_indicator = MACD_range_values
            rule.append(MACD_value_third_indicator)
            options_list.append(MACD_EMA_slow_option_third_indicator)
            options_list.append(MACD_EMA_fast_option_third_indicator)
            options_list.append(MACD_SMA_option_third_indicator)
            values_list.append(MACD_value_third_indicator)
            rulem.append(MACD_value_third_indicator)
            options_listm.append(MACD_EMA_slow_option_third_indicator)
            options_listm.append(MACD_EMA_fast_option_third_indicator)
            options_listm.append(MACD_SMA_option_third_indicator)
            values_listm.append(MACD_value_third_indicator)
            
                
        if third_indicator == 2: #RSI choice
            indicator_list.append('RSI')
            indicator_listm.append('RSI')
            RSI_option_third_indicator = RSI_range_options[random.randint(0,4)]
            rule.append(RSI_option_third_indicator)
            options_list.append(RSI_option_third_indicator)
            rulem.append(RSI_option_third_indicator)
            options_listm.append(RSI_option_third_indicator)
            RSI_value_third_indicator = RSI_range_values
            rule.append(RSI_value_third_indicator)
            values_list.append(RSI_value_third_indicator)
            rulem.append(RSI_value_third_indicator)
            values_listm.append(RSI_value_third_indicator)
                
        if third_indicator == 3: #Momentum choice
            indicator_list.append('Momentum')
            indicator_listm.append('Momentum')
            Momentum_option_third_indicator = Momentum_range_options
            rule.append(Momentum_option_third_indicator)
            options_list.append(Momentum_option_third_indicator)
            rulem.append(Momentum_option_third_indicator)
            options_listm.append(Momentum_option_third_indicator)
            Momentum_value_third_indicator = round(random.uniform(92.48,109.81),2)
            rule.append(Momentum_value_third_indicator)
            values_list.append(Momentum_value_third_indicator)
            rulem.append(Momentum_value_third_indicator)
            values_listm.append(Momentum_value_third_indicator)
            
        first_comparator = list_comparators[random.randint(0,5)]
        rule.append(first_comparator)
        rulem.append(first_comparator)
        comp_list.append(first_comparator)
        comp_listm.append(first_comparator)
        second_comparator = list_comparators[random.randint(0,5)]
        rule.append(second_comparator)
        comp_list.append(second_comparator)
        rulem.append(second_comparator)
        comp_listm.append(second_comparator)
        third_comparator = list_comparators[random.randint(0,5)]
        rule.append(third_comparator)
        comp_list.append(third_comparator)
        rulem.append(third_comparator)
        comp_listm.append(third_comparator)
        
        first_logical_operator = list_logical[random.randint(0,1)]
        rule.append(first_logical_operator)
        log_op_list.append(first_logical_operator)
        rulem.append(first_logical_operator)
        log_op_listm.append(first_logical_operator)
        second_logical_operator = list_logical[random.randint(0,1)] 
        rule.append(second_logical_operator)
        log_op_list.append(second_logical_operator)
        rulem.append(second_logical_operator)
        log_op_listm.append(second_logical_operator)
        
        order = list_orders[random.randint(0,1)]
        rule.append(order)
        rulem.append(order)
        
        ### BEGINNING PART WHERE THE NUMBER OF INDICATORS EQUALS  4   ###
    if number_indicators == 4:
        first_indicator = random.randint(0,3)
        rule.append(first_indicator)
        rulem.append(first_indicator)
        second_indicator = random.randint(0,3)
        rule.append(second_indicator)
        rulem.append(second_indicator)
        third_indicator = random.randint(0,3)
        rule.append(third_indicator)
        rulem.append(third_indicator)
        fourth_indicator = random.randint(0,3)
        rule.append(fourth_indicator)
        rulem.append(fourth_indicator)
        
        if first_indicator == 0: #SMA choice
            indicator_list.append('SMA')
            indicator_listm.append('SMA')
            SMA_option_first_indicator = SMA_range_options[random.randint(0,6)]
            rule.append(SMA_option_first_indicator)
            options_list.append(SMA_option_first_indicator)
            rulem.append(SMA_option_first_indicator)
            options_listm.append(SMA_option_first_indicator)
            SMA_value_first_indicator = SMA_range_values[random.randint(0,10)]
            rule.append(SMA_value_first_indicator)
            values_list.append(SMA_value_first_indicator)
            rulem.append(SMA_value_first_indicator)
            values_listm.append(SMA_value_first_indicator)
            #SMA values to be determined , see backtrader so choose OHLC value of last bar
                
        if first_indicator == 1: #MACD choice
            indicator_list.append('MACD')
            indicator_listm.append('MACD')
            MACD_EMA_fast_option_first_indicator = MACD_range_options_EMA_fast[random.randint(0,1)]
            MACD_EMA_slow_option_first_indicator = MACD_range_options_EMA_slow[random.randint(0,1)]
            rule.append(MACD_EMA_slow_option_first_indicator)
            rule.append(MACD_EMA_fast_option_first_indicator)
            rulem.append(MACD_EMA_slow_option_first_indicator)
            rulem.append(MACD_EMA_fast_option_first_indicator)
            MACD_SMA_option_first_indicator = MACD_range_options_SMA[random.randint(0,1)]
            rule.append(MACD_SMA_option_first_indicator)
            rulem.append(MACD_SMA_option_first_indicator)
            MACD_value_first_indicator = MACD_range_values
            rule.append(MACD_value_first_indicator)
            options_list.append(MACD_EMA_slow_option_first_indicator)
            options_list.append(MACD_EMA_fast_option_first_indicator)
            options_list.append(MACD_SMA_option_first_indicator)
            values_list.append(MACD_value_first_indicator)
            rulem.append(MACD_value_first_indicator)
            options_listm.append(MACD_EMA_slow_option_first_indicator)
            options_listm.append(MACD_EMA_fast_option_first_indicator)
            options_listm.append(MACD_SMA_option_first_indicator)
            values_listm.append(MACD_value_first_indicator)
                
        if first_indicator == 2: #RSI choice
            indicator_list.append('RSI')
            indicator_listm.append('RSI')
            RSI_option_first_indicator = RSI_range_options[random.randint(0,4)]
            rule.append(RSI_option_first_indicator)
            options_list.append(RSI_option_first_indicator)
            rulem.append(RSI_option_first_indicator)
            options_listm.append(RSI_option_first_indicator)
            RSI_value_first_indicator = RSI_range_values
            rule.append(RSI_value_first_indicator)
            values_list.append(RSI_value_first_indicator)
            rulem.append(RSI_value_first_indicator)
            values_listm.append(RSI_value_first_indicator)
                
        if first_indicator == 3: #Momentum choice
            indicator_list.append('Momentum')
            indicator_listm.append('Momentum')
            Momentum_option_first_indicator = Momentum_range_options
            rule.append(Momentum_option_first_indicator)
            options_list.append(Momentum_range_options)
            rulem.append(Momentum_option_first_indicator)
            options_listm.append(Momentum_range_options)
            Momentum_value_first_indicator = round(random.uniform(92.48,109.81),2)
            rule.append(Momentum_value_first_indicator)
            values_list.append(Momentum_value_first_indicator)  
            rulem.append(Momentum_value_first_indicator)
            values_listm.append(Momentum_value_first_indicator)  
             #SECOND INDICATOR PART   
                
        if second_indicator == 0: #SMA choice
            indicator_list.append('SMA')
            indicator_listm.append('SMA')
            SMA_option_second_indicator = SMA_range_options[random.randint(0,6)]
            rule.append(SMA_option_second_indicator)
            options_list.append(SMA_option_second_indicator)
            rulem.append(SMA_option_second_indicator)
            options_listm.append(SMA_option_second_indicator)
            SMA_value_second_indicator = SMA_range_values[random.randint(0,10)]
            rule.append(SMA_value_second_indicator)
            values_list.append(SMA_value_second_indicator)
            rulem.append(SMA_value_second_indicator)
            values_listm.append(SMA_value_second_indicator)
            #SMA values to be determined , see backtrader so choose OHLC value of last bar
                
        if second_indicator == 1: #MACD choice
            indicator_list.append('MACD')
            indicator_listm.append('MACD')
            MACD_EMA_fast_option_second_indicator = MACD_range_options_EMA_fast[random.randint(0,1)]
            MACD_EMA_slow_option_second_indicator = MACD_range_options_EMA_slow[random.randint(0,1)]
            rule.append(MACD_EMA_slow_option_second_indicator)
            rule.append(MACD_EMA_fast_option_second_indicator)
            rulem.append(MACD_EMA_slow_option_second_indicator)
            rulem.append(MACD_EMA_fast_option_second_indicator)
            MACD_SMA_option_second_indicator = MACD_range_options_SMA[random.randint(0,1)]
            rule.append(MACD_SMA_option_second_indicator)
            rulem.append(MACD_SMA_option_second_indicator)
            MACD_value_second_indicator = MACD_range_values
            rule.append(MACD_value_second_indicator)
            options_list.append(MACD_EMA_slow_option_second_indicator)
            options_list.append(MACD_EMA_fast_option_second_indicator)
            options_list.append(MACD_SMA_option_second_indicator)
            values_list.append(MACD_value_second_indicator)
            rulem.append(MACD_value_second_indicator)
            options_listm.append(MACD_EMA_slow_option_second_indicator)
            options_listm.append(MACD_EMA_fast_option_second_indicator)
            options_listm.append(MACD_SMA_option_second_indicator)
            values_listm.append(MACD_value_second_indicator)
                
        if second_indicator == 2: #RSI choice
            indicator_list.append('RSI')
            indicator_listm.append('RSI')
            RSI_option_second_indicator = RSI_range_options[random.randint(0,4)]
            rule.append(RSI_option_second_indicator)
            options_list.append(RSI_option_second_indicator)
            rulem.append(RSI_option_second_indicator)
            options_listm.append(RSI_option_second_indicator)
            RSI_value_second_indicator = RSI_range_values
            rule.append(RSI_value_second_indicator)
            values_list.append(RSI_value_second_indicator)
            rulem.append(RSI_value_second_indicator)
            values_listm.append(RSI_value_second_indicator)
            
                
        if second_indicator == 3: #Momentum choice
            indicator_list.append('Momentum')
            indicator_listm.append('Momentum')
            Momentum_option_second_indicator = Momentum_range_options
            rule.append(Momentum_option_second_indicator)
            options_list.append(Momentum_option_second_indicator)
            rulem.append(Momentum_option_second_indicator)
            options_listm.append(Momentum_option_second_indicator)
            Momentum_value_second_indicator = round(random.uniform(92.48,109.81),2)
            rule.append(Momentum_value_second_indicator)
            values_list.append(Momentum_value_second_indicator)
            rulem.append(Momentum_value_second_indicator)
            values_listm.append(Momentum_value_second_indicator)
                
                #3rd indicator part#
                
        if third_indicator == 0: #SMA choice
            indicator_list.append('SMA')
            indicator_listm.append('SMA')
            SMA_option_third_indicator = SMA_range_options[random.randint(0,6)]
            rule.append(SMA_option_third_indicator)
            options_list.append(SMA_option_third_indicator)
            rulem.append(SMA_option_third_indicator)
            options_listm.append(SMA_option_third_indicator)
            SMA_value_third_indicator = SMA_range_values[random.randint(0,10)]
            rule.append(SMA_value_third_indicator)
            values_list.append(SMA_value_third_indicator)
            rulem.append(SMA_value_third_indicator)
            values_listm.append(SMA_value_third_indicator)
            #SMA values to be determined , see backtrader so choose OHLC value of last bar
                
        if third_indicator == 1: #MACD choice
            indicator_list.append('MACD')
            indicator_listm.append('MACD')
            MACD_EMA_fast_option_third_indicator = MACD_range_options_EMA_fast[random.randint(0,1)]
            MACD_EMA_slow_option_third_indicator = MACD_range_options_EMA_slow[random.randint(0,1)]
            rule.append(MACD_EMA_slow_option_third_indicator)
            rule.append(MACD_EMA_fast_option_third_indicator)
            rulem.append(MACD_EMA_slow_option_third_indicator)
            rulem.append(MACD_EMA_fast_option_third_indicator)
            MACD_SMA_option_third_indicator = MACD_range_options_SMA[random.randint(0,1)]
            rule.append(MACD_SMA_option_third_indicator)
            rulem.append(MACD_SMA_option_third_indicator)
            MACD_value_third_indicator = MACD_range_values
            rule.append(MACD_value_third_indicator)
            options_list.append(MACD_EMA_slow_option_third_indicator)
            options_list.append(MACD_EMA_fast_option_third_indicator)
            options_list.append(MACD_SMA_option_third_indicator)
            values_list.append(MACD_value_third_indicator)
            rulem.append(MACD_value_third_indicator)
            options_listm.append(MACD_EMA_slow_option_third_indicator)
            options_listm.append(MACD_EMA_fast_option_third_indicator)
            options_listm.append(MACD_SMA_option_third_indicator)
            values_listm.append(MACD_value_third_indicator)
                
        if third_indicator == 2: #RSI choice
            indicator_list.append('RSI')
            indicator_listm.append('RSI')
            RSI_option_third_indicator = RSI_range_options[random.randint(0,4)]
            rule.append(RSI_option_third_indicator)
            options_list.append(RSI_option_third_indicator)
            rulem.append(RSI_option_third_indicator)
            options_listm.append(RSI_option_third_indicator)
            RSI_value_third_indicator = RSI_range_values
            rule.append(RSI_value_third_indicator)
            values_list.append(RSI_value_third_indicator)
            rulem.append(RSI_value_third_indicator)
            values_listm.append(RSI_value_third_indicator)
                
        if third_indicator == 3: #Momentum choice
            indicator_list.append('Momentum')
            indicator_listm.append('Momentum')
            Momentum_option_third_indicator = Momentum_range_options
            rule.append(Momentum_option_third_indicator)
            options_list.append(Momentum_option_third_indicator)
            rulem.append(Momentum_option_third_indicator)
            options_listm.append(Momentum_option_third_indicator)
            Momentum_value_third_indicator = round(random.uniform(92.48,109.81),2)
            rule.append(Momentum_value_third_indicator)
            values_list.append(Momentum_value_third_indicator)
            rulem.append(Momentum_value_third_indicator)
            values_listm.append(Momentum_value_third_indicator)
            
        if fourth_indicator == 0: #SMA choice
            indicator_list.append('SMA')
            indicator_listm.append('SMA')
            SMA_option_fourth_indicator = SMA_range_options[random.randint(0,6)]
            rule.append(SMA_option_fourth_indicator)
            options_list.append(SMA_option_fourth_indicator)
            rulem.append(SMA_option_fourth_indicator)
            options_listm.append(SMA_option_fourth_indicator)
            SMA_value_fourth_indicator = SMA_range_values[random.randint(0,10)]
            rule.append(SMA_value_fourth_indicator)
            values_list.append(SMA_value_fourth_indicator)
            rulem.append(SMA_value_fourth_indicator)
            values_listm.append(SMA_value_fourth_indicator)
            #SMA values to be determined , see backtrader so choose OHLC value of last bar
                
        if fourth_indicator == 1: #MACD choice
            indicator_list.append('MACD')
            indicator_listm.append('MACD')
            MACD_EMA_fast_option_fourth_indicator = MACD_range_options_EMA_fast[random.randint(0,1)]
            MACD_EMA_slow_option_fourth_indicator = MACD_range_options_EMA_slow[random.randint(0,1)]
            rule.append(MACD_EMA_slow_option_fourth_indicator)
            rule.append(MACD_EMA_fast_option_fourth_indicator)
            rulem.append(MACD_EMA_slow_option_fourth_indicator)
            rulem.append(MACD_EMA_fast_option_fourth_indicator)
            MACD_SMA_option_fourth_indicator = MACD_range_options_SMA[random.randint(0,1)]
            rule.append(MACD_SMA_option_fourth_indicator)
            rulem.append(MACD_SMA_option_fourth_indicator)
            MACD_value_fourth_indicator = MACD_range_values
            rule.append(MACD_value_fourth_indicator)
            options_list.append(MACD_EMA_slow_option_fourth_indicator)
            options_list.append(MACD_EMA_fast_option_fourth_indicator)
            options_list.append(MACD_SMA_option_fourth_indicator)
            values_list.append(MACD_value_fourth_indicator)
            rulem.append(MACD_value_fourth_indicator)
            options_listm.append(MACD_EMA_slow_option_fourth_indicator)
            options_listm.append(MACD_EMA_fast_option_fourth_indicator)
            options_listm.append(MACD_SMA_option_fourth_indicator)
            values_listm.append(MACD_value_fourth_indicator)
                
        if fourth_indicator == 2: #RSI choice
            indicator_list.append('RSI')
            indicator_listm.append('RSI')
            RSI_option_fourth_indicator = RSI_range_options[random.randint(0,4)]
            rule.append(RSI_option_fourth_indicator)
            options_list.append(RSI_option_fourth_indicator)
            rulem.append(RSI_option_fourth_indicator)
            options_listm.append(RSI_option_fourth_indicator)
            RSI_value_fourth_indicator = RSI_range_values
            rule.append(RSI_value_fourth_indicator)
            values_list.append(RSI_value_fourth_indicator)
            rulem.append(RSI_value_fourth_indicator)
            values_listm.append(RSI_value_fourth_indicator)
                
        if fourth_indicator == 3: #Momentum choice
            indicator_list.append('Momentum')
            indicator_listm.append('Momentum')
            Momentum_option_fourth_indicator = Momentum_range_options
            rule.append(Momentum_option_fourth_indicator)
            options_list.append(Momentum_option_fourth_indicator)
            rulem.append(Momentum_option_fourth_indicator)
            options_listm.append(Momentum_option_fourth_indicator)
            Momentum_value_fourth_indicator = round(random.uniform(92.48,109.81),2)
            rule.append(Momentum_value_fourth_indicator)
            values_list.append(Momentum_value_fourth_indicator)
            rulem.append(Momentum_value_fourth_indicator)
            values_listm.append(Momentum_value_fourth_indicator)
            
        first_comparator = list_comparators[random.randint(0,5)]
        rule.append(first_comparator)
        comp_list.append(first_comparator)
        rulem.append(first_comparator)
        comp_listm.append(first_comparator)
        second_comparator = list_comparators[random.randint(0,5)]
        rule.append(second_comparator)
        comp_list.append(second_comparator)
        rulem.append(second_comparator)
        comp_listm.append(second_comparator)
        third_comparator = list_comparators[random.randint(0,5)]
        rule.append(third_comparator)
        comp_list.append(third_comparator)
        rulem.append(third_comparator)
        comp_listm.append(third_comparator)
        
        fourth_comparator = list_comparators[random.randint(0,5)]
        rule.append(fourth_comparator)
        comp_list.append(fourth_comparator)
        rulem.append(fourth_comparator)
        comp_listm.append(fourth_comparator)

        
        first_logical_operator = list_logical[random.randint(0,1)] 
        rule.append(first_logical_operator)
        log_op_list.append(first_logical_operator)
        rulem.append(first_logical_operator)
        log_op_listm.append(first_logical_operator)
        second_logical_operator = list_logical[random.randint(0,1)] 
        rule.append(second_logical_operator)
        log_op_list.append(second_logical_operator)
        rulem.append(second_logical_operator)
        log_op_listm.append(second_logical_operator)
        third_logical_operator = list_logical[random.randint(0,1)]
        rule.append(third_logical_operator)
        log_op_list.append(third_logical_operator)
        rulem.append(third_logical_operator)
        log_op_listm.append(third_logical_operator)
        
        order = list_orders[random.randint(0,1)]
        rule.append(order)
        rulem.append(order)
        
    
        
    
    
#    print(options_list)
    return rule
            

                        
                        


def create_member():
    global count
    global member
    global rule
    global first_rule
    global options_list
    global indicator_list
    global comp_list
    global log_op_list
    global values_list
    global variable_name
    print('count before writing in python :'+str(count))
    member=[]
    member.append(create_rule())
    first_order = rule[-1]
    first_rule = member[0] 
    write_in_python_file(member[0],member[0][0])
    rule = []
    options_list = []
    indicator_list = []
    comp_list = []
    log_op_list = []
    values_list  = []
       
    create_rule()

    
    
    second_order = rule[-1]
        
    if first_order == second_order:
        if second_order == 0:
            rule[-1] = 1
            member.append(rule)
                
        else:
            rule[-1] = 0
            member.append(rule)
    else:
        member.append(rule)
    write_in_python_file(member[1],member[1][0])
    print('count after writing in python:'+str(count))
        
#    for value in member:
#        print(value)
    
    return member
    
    
        
        



  
#print(create_member())

#print(len(create_rule()))
#create_rule()

#for value in rule:
#    print(value)
#     
def write_in_python_file(rule, number_indicators):
    global options_list
    global indicator_list
    global comp_list
    global log_op_list
    global values_list
    global count
    
     
    
#    test = open('rule_writing.txt','w')
#    test.write(str(rule)+"\n")
#    test.close()
        
#    for value in options_list:
#        print(value)
#    print(len(options_list))
#    print(number_indicators)

    if rule[-1] == 1:
        order_type = 'buy'
    else:
        order_type = 'sell'
    
    
    if number_indicators == 2:
        
        if comp_list[0] == 0:
            comp1 = '<'
        if comp_list[0] == 1:
            comp1 = '<='
        if comp_list[0] == 2:
            comp1 = '>'
        if comp_list[0] == 3:
            comp1 = '>='
        if comp_list[0] == 4:
            comp1 = '=='
        if comp_list[0] == 5:
            comp1 = '!='
            
        if comp_list[1] == 0:
            comp2 = '<'
        if comp_list[1] == 1:
            comp2 = '<='
        if comp_list[1] == 2:
            comp2 = '>'
        if comp_list[1] == 3:
            comp2 = '>='
        if comp_list[1] == 4:
            comp2 = '=='
        if comp_list[1] == 5:
            comp2 = '!='
        
        if log_op_list[0] == 0:
            logicalop = 'and'
        else:
            logicalop = 'or'
        
        value1 = values_list[0]
        value2 = values_list[1]
        print('length of begining options list : '+str(len(options_list)))
        print('printing values of beg options list :')
        for val in options_list:
            print(val)
        
        if len(options_list) == 6:
            print('enter when list lenght = 6')
            print('length of options list : '+str(len(options_listm)))
            for item in options_listm:
                print(item)
            print(indicator_listm)
            option1_1 = options_list[0]
            option1_2 = options_list[1]
            option1_3 = options_list[2]
            option2_1 = options_list[3]
            option2_2 = options_list[4]
            option2_3 = options_list[5]
            rule1 = open('rule_writing.txt','a')
            if count == 0:
                if(indicator_listm[0] == 'MACD' and indicator_listm[1] == 'MACD'):
                    number_macd1 = str(random.randint(0,2))
                    number_macd2 = str(random.randint(3,5))
                    rule1.write("\t\tself.MACD" +number_macd1 +  " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[0]) +",period_me2 =" + str(options_listm[1]) + ",period_signal =" + str(options_listm[2]) + ")\n")
                    rule1.write("\t\tself.MACD"+number_macd2 + " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[3]) +",period_me2 =" + str(options_listm[4]) + ",period_signal =" + str(options_listm[5]) + ")\n")
                    variable_name.append("self.MACD" +number_macd1)
                    variable_name.append("self.MACD" +number_macd2)
            if count ==1:
                if (indicator_listm[0] == 'MACD' and indicator_listm[1] != 'MACD') or (indicator_listm[0] != 'MACD' and indicator_listm[1] == 'MACD'):                   
                    number_macd1 = str(random.randint(3,5))
                    number_macd2 = str(random.randint(6,8))                    
                    rule1.write("\t\tself.MACD" +number_macd1 +  " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[4]) +",period_me2 =" + str(options_listm[5]) + ",period_signal =" + str(options_listm[6]) + ")\n")                    
                    variable_name.append("self.MACD" +number_macd1)
                    rule1.write("\t\tself.MACD"+number_macd2 + " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[7]) +",period_me2 =" + str(options_listm[8]) + ",period_signal =" + str(options_listm[9]) + ")\n")
                    variable_name.append("self.MACD" +number_macd2)
                if (indicator_listm[0] != 'MACD' and indicator_listm[1] != 'MACD'):
                    number_macd1 = str(random.randint(3,5))
                    number_macd2 = str(random.randint(6,8))
                    rule1.write("\t\tself.MACD" +number_macd1 +  " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[2]) +",period_me2 =" + str(options_listm[3]) + ",period_signal =" + str(options_listm[4]) + ")\n")                    
                    variable_name.append("self.MACD" +number_macd1)
                    rule1.write("\t\tself.MACD"+number_macd2 + " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[5]) +",period_me2 =" + str(options_listm[6]) + ",period_signal =" + str(options_listm[7]) + ")\n")
                    variable_name.append("self.MACD" +number_macd2)
                if (indicator_listm[0] == 'MACD' and indicator_listm[1] == 'MACD'):
                    number_macd1 = str(random.randint(3,5))
                    number_macd2 = str(random.randint(6,8))
                    rule1.write("\t\tself.MACD" +number_macd1 +  " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[6]) +",period_me2 =" + str(options_listm[7]) + ",period_signal =" + str(options_listm[8]) + ")\n")                    
                    variable_name.append("self.MACD" +number_macd1)
                    rule1.write("\t\tself.MACD"+number_macd2 + " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[6]) +",period_me2 =" + str(options_listm[7]) + ",period_signal =" + str(options_listm[8]) + ")\n")
                    variable_name.append("self.MACD" +number_macd2)
#            rule1.write("self."+str(indicator_list[0]) + " =bt.indicators."+str(indicator_list[0]) )
#            rule1.write("if("+str(indicator_list[0]) + "("+ str(option1_1)+"'"+
#                                 str(option1_2)+"'"+str(option1_3)+")"+
#                                comp1 + str(value1) + str(logicalop)+
#                                str(indicator_list[1]) + "("+ str(option2_1)+"'"+
#                                 str(option2_2)+"'"+str(option2_3)+")" +comp2+str(value2)+
#                                ") \n\tself."+order_type+"()")
            print(variable_name)
            rule1.close()  
            

        
        elif len(options_list) == 4:
            print('entered when length option list = 4')
            print('length of optionsm list : '+str(len(options_listm)))
            for item in options_listm:
                print(item)
            print(indicator_listm)
            if count == 0:
#            if indicator_listm[0] == 'MACD':  
                option1_1 = options_list[0]
                option1_2 = options_list[1]
                option1_3 = options_list[2]
                option2 = options_list[3]
                rule1 = open('rule_writing.txt','a')
#                if count == 0: 
                print(indicator_listm[0])
                if indicator_listm[0] == 'MACD':
#                    if indicator_listm[0] == 'MACD':                       
                    number_macd1 = str(random.randint(0,2))
                    rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[0]) +",period_me2 =" + str(options_listm[1]) + ",period_signal =" + str(options_listm[2]) + ")\n")
                    variable_name.append("self.MACD" +number_macd1)
#                    rule1.write("self.MACD2" + " = bt.indicators.MACD" + "(self.data , period_me1 =" + options_list[0] ,",period_me2 =" + options_list[1] + ",period_signal =" + options_list[2] + ")")
                    if indicator_listm[1] == 'SMA':
                        number_sma = str(random.randint(0,2))
                        rule1.write("\t\tself.SMA"+number_sma+ " = bt.indicators.SMA" + "(self.datas[0] , period =" + str(options_listm[3])+ ")\n")
                        variable_name.append("self.SMA" +number_sma)
                    elif (indicator_listm[1] == 'RSI'):
                        number_rsi = str(random.randint(0,2))
                        rule1.write("\t\tself.RSI" +number_rsi+" = bt.indicators.RSI" + "(period = " + str(options_listm[3]) + ")\n")
                        variable_name.append("self.RSI" +number_rsi)
                    elif (indicator_listm[1] == 'Momentum'):
                        number_mom = str(random.randint(0,2))
                        rule1.write("\t\tself.Momentum" +number_mom+" = bt.indicators.Momentum" + "(period = " + str(options_listm[3]) + ")\n")
                        variable_name.append("self.Momentum" +number_mom)
                if indicator_listm[0] != 'MACD':
                    if indicator_listm[0] == 'SMA':
                        number_sma = str(random.randint(3,5))
                        rule1.write("\t\tself.SMA "+number_sma+ " = bt.indicators.SMA" + "(self.datas[0] , period =" + str(options_listm[0])+ ")\n")
                        variable_name.append("self.SMA" +number_sma)
#                        if indicator_listm[1] == 'MACD':                        
                        number_macd1 = str(random.randint(3,5))
                        rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[1]) +",period_me2 =" + str(options_listm[2]) + ",period_signal =" + str(options_listm[3]) + ")\n")
                        variable_name.append("self.MACD" +number_macd1)
                    elif (indicator_listm[0] == 'RSI'):
                        number_rsi = str(random.randint(3,5))
                        rule1.write("\t\tself.RSI" +number_rsi+" = bt.indicators.RSI" + "(period = " + str(options_listm[0]) + ")\n")
                        variable_name.append("self.RSI" +number_rsi)
#                        if indicator_listm[1] == 'MACD':                        
                        number_macd1 = str(random.randint(3,5))
                        rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[1]) +",period_me2 =" + str(options_listm[2]) + ",period_signal =" + str(options_listm[3]) + ")\n")
                        variable_name.append("self.MACD" +number_macd1)
                    elif (indicator_listm[0] == 'Momentum'):
                        number_mom = str(random.randint(3,5))
                        rule1.write("\t\tself.Momentum" +number_mom+" = bt.indicators.Momentum" + "(period = " + str(options_listm[0]) + ")\n")
                        variable_name.append("self.Momentum" +number_mom)
#                        if indicator_listm[1] == 'MACD':                        
                        number_macd1 = str(random.randint(3,5))
                        rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[1]) +",period_me2 =" + str(options_listm[2]) + ",period_signal =" + str(options_listm[3]) + ")\n")
                        variable_name.append("self.MACD" +number_macd1)
#                else:
#                    number_macd1 = str(random.randint(0,2))
#                    rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[0]) +",period_me2 =" + str(options_listm[1]) + ",period_signal =" + str(options_listm[2]) + ")\n")
            if count ==1:
                print('entered when length = 47 and count = 1 ')
                rule1 = open('rule_writing.txt','a') 
                if indicator_listm[2] == 'MACD':
#                    if indicator_listm[1] == 'SMA':
#                        rule1.write("\t\tself.SMA "+ " = bt.indicators.SMA" + "(self.datas[0] , period =" + str(options_listm[0])+ ")\n")
#                    elif (indicator_listm[1] == 'RSI'):
#                        rule1.write("\t\tself.RSI" +" = bt.indicators.RSI" + "(period = " + str(options_listm[0]) + ")\n")
#                    elif (indicator_listm[1] == 'Momentum'):
#                        rule1.write("\t\tself.Momentum" +" = bt.indicators.Momentum" + "(period = " + str(options_listm[0]) + ")\n")
                    if (indicator_listm[0] == 'MACD' and indicator_listm[1] == 'MACD'):
                        number_macd1 = str(random.randint(7,9))  
    #                    rule1.close()
                        rule1 = open('rule_writing.txt','a')      
                        rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[6]) +",period_me2 =" + str(options_listm[7]) + ",period_signal =" + str(options_listm[8]) + ")\n")
                        variable_name.append("self.MACD" +number_macd1)
    #                    rule1.write("self.MACD2" + " = bt.indicators.MACD" + "(self.data , period_me1 =" + options_list[0] ,",period_me2 =" + options_list[1] + ",period_signal =" + options_list[2] + ")")
                        if indicator_listm[3] == 'SMA':
                            number_sma = str(random.randint(7,9))
                            rule1.write("\t\tself.SMA"+number_sma+ " = bt.indicators.SMA" + "(self.datas[0] , period =" + str(options_listm[9])+ ")\n")
                            variable_name.append("self.SMA" +number_sma)
                        elif (indicator_listm[3] == 'RSI'):
                            number_rsi = str(random.randint(7,9))
                            rule1.write("\t\tself.RSI" +number_rsi+" = bt.indicators.RSI" + "(period = " + str(options_listm[9]) + ")\n")
                            variable_name.append("self.RSI" +number_rsi)
                        elif (indicator_listm[3] == 'Momentum'):
                            number_mom = str(random.randint(7,9))
                            rule1.write("\t\tself.Momentum" +number_mom+" = bt.indicators.Momentum" + "(period = " + str(options_listm[9]) + ")\n")
                            variable_name.append("self.Momentum" +number_mom)
                    if (indicator_listm[0] != 'MACD' and indicator_listm[1] == 'MACD')or (indicator_listm[0] == 'MACD' and indicator_listm[1] != 'MACD'): 
                        number_macd1 = str(random.randint(7,9))  
    #                    rule1.close()
#                        rule1 = open('rule_writing.txt','a')
#                        rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[4]) +",period_me2 =" + str(options_listm[5]) + ",period_signal =" + str(options_listm[6]) + ")\n")
    #                    rule1.write("self.MACD2" + " = bt.indicators.MACD" + "(self.data , period_me1 =" + options_list[0] ,",period_me2 =" + options_list[1] + ",period_signal =" + options_list[2] + ")")
    
                        if indicator_listm[2] == 'SMA':
                            number_sma = str(random.randint(10,12))
                            rule1.write("\t\tself.SMA"+number_sma+ " = bt.indicators.MACD" + "(self.datas[0] , period =" + str(options_listm[4])+ ")\n")
                            variable_name.append("self.SMA" +number_sma)
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[5]) +",period_me2 =" + str(options_listm[6]) + ",period_signal =" + str(options_listm[7]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                        elif (indicator_listm[2] == 'RSI'):
                            number_rsi = str(random.randint(10,12))
                            rule1.write("\t\tself.RSI" +number_rsi+" = bt.indicators.RSI" + "(period = " + str(options_listm[4]) + ")\n")
                            variable_name.append("self.RSI" +number_rsi)
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[5]) +",period_me2 =" + str(options_listm[6]) + ",period_signal =" + str(options_listm[7]) + ")\n") 
                            variable_name.append("self.MACD" +number_macd1)
                        elif (indicator_listm[2] == 'Momentum'):
                            number_mom = str(random.randint(10,12))
                            rule1.write("\t\tself.Momentum" +number_mom+" = bt.indicators.Momentum" + "(period = " + str(options_listm[4]) + ")\n")
                            variable_name.append("self.Momentum" +number_mom)
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[5]) +",period_me2 =" + str(options_listm[6]) + ",period_signal =" + str(options_listm[7]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                        if indicator_listm[3] == 'SMA':
                            number_sma = str(random.randint(10,12))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[4]) +",period_me2 =" + str(options_listm[5]) + ",period_signal =" + str(options_listm[6]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                            rule1.write("\t\tself.SMA"+number_sma+ " = bt.indicators.MACD" + "(self.datas[0] , period =" + str(options_listm[7])+ ")\n")
                            variable_name.append("self.SMA" +number_sma)
                        elif (indicator_listm[3] == 'RSI'):
                            number_rsi = str(random.randint(10,12))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[4]) +",period_me2 =" + str(options_listm[5]) + ",period_signal =" + str(options_listm[6]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                            rule1.write("\t\tself.RSI" +number_rsi+" = bt.indicators.RSI" + "(period = " + str(options_listm[7]) + ")\n")
                            variable_name.append("self.RSI" +number_rsi)
                        elif (indicator_listm[3] == 'Momentum'):
                            number_mom = str(random.randint(10,12))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[4]) +",period_me2 =" + str(options_listm[5]) + ",period_signal =" + str(options_listm[6]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                            rule1.write("\t\tself.Momentum" +number_mom+" = bt.indicators.Momentum" + "(period = " + str(options_listm[7]) + ")\n")
                            variable_name.append("self.Momentum" +number_mom)
                    if (indicator_listm[0] != 'MACD' and indicator_listm[1] != 'MACD'): 
                          
    #                    rule1.close()
#                        rule1 = open('rule_writing.txt','a')                      
#                        rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[2]) +",period_me2 =" + str(options_listm[3]) + ",period_signal =" + str(options_listm[4]) + ")\n")
    #                    rule1.write("self.MACD2" + " = bt.indicators.MACD" + "(self.data , period_me1 =" + options_list[0] ,",period_me2 =" + options_list[1] + ",period_signal =" + options_list[2] + ")")
                        if indicator_listm[2] == 'MACD':
                            number_macd1 = str(random.randint(13,15))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[2]) +",period_me2 =" + str(options_listm[3]) + ",period_signal =" + str(options_listm[4]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                        if indicator_listm[2] == 'SMA':
                            number_sma = str(random.randint(13,15))
                            rule1.write("\t\tself.SMA"+number_sma+ " = bt.indicators.MACD" + "(self.datas[0] , period =" + str(options_listm[5])+ ")\n")
                            variable_name.append("self.SMA" +number_sma)
                        elif (indicator_listm[2] == 'RSI'):
                            number_rsi = str(random.randint(13,15))
                            rule1.write("\t\tself.RSI" +number_rsi+" = bt.indicators.RSI" + "(period = " + str(options_listm[5]) + ")\n")
                            variable_name.append("self.RSI" +number_rsi)
                        elif (indicator_listm[2] == 'Momentum'):
                            number_mom = str(random.randint(13,15))
                            rule1.write("\t\tself.Momentum" +number_mom+" = bt.indicators.Momentum" + "(period = " + str(options_listm[5]) + ")\n")
                            variable_name.append("self.Momentum" +number_mom)
                        if indicator_listm[3] == 'SMA':
                            number_sma = str(random.randint(13,15))
                            rule1.write("\t\tself.SMA"+number_sma+ " = bt.indicators.MACD" + "(self.datas[0] , period =" + str(options_listm[5])+ ")\n")
                            variable_name.append("self.SMA" +number_sma)
                        elif (indicator_listm[3] == 'RSI'):
                            number_rsi = str(random.randint(13,15))
                            rule1.write("\t\tself.RSI" +number_rsi+" = bt.indicators.RSI" + "(period = " + str(options_listm[5]) + ")\n")
                            variable_name.append("self.RSI" +number_rsi)
                        elif (indicator_listm[3] == 'Momentum'):
                            number_mom = str(random.randint(13,15))
                            rule1.write("\t\tself.Momentum" +number_mom+" = bt.indicators.Momentum" + "(period = " + str(options_listm[5]) + ")\n")
                            variable_name.append("self.Momentum" +number_mom)
                        if indicator_listm[3] == 'MACD':
                            number_macd1 = str(random.randint(13,15))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[3]) +",period_me2 =" + str(options_listm[4]) + ",period_signal =" + str(options_listm[5]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                if indicator_listm[2] != 'MACD' :
                    if indicator_listm[0] != 'MACD' and indicator_listm[1] != 'MACD':
                        if indicator_listm[2] == 'SMA':
                            number_sma = str(random.randint(17,19))
                            rule1.write("\t\tself.SMA "+ " = bt.indicators.MACD" + "(self.datas[0] , period =" + str(options_listm[2])+ ")\n")
                            variable_name.append("self.SMA" +number_sma)
                            number_macd1 = str(random.randint(17,19))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[3]) +",period_me2 =" + str(options_listm[4]) + ",period_signal =" + str(options_listm[5]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                        elif (indicator_listm[2] == 'RSI'):
                            number_rsi = str(random.randint(17,19))
                            rule1.write("\t\tself.RSI" +" = bt.indicators.RSI" + "(period = " + str(options_listm[2]) + ")\n")
                            variable_name.append("self.RSI" +number_rsi)
                            number_macd1 = str(random.randint(17,19))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[3]) +",period_me2 =" + str(options_listm[4]) + ",period_signal =" + str(options_listm[5]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                        elif (indicator_listm[2] == 'Momentum'):
                            number_mom = str(random.randint(17,19))
                            rule1.write("\t\tself.Momentum" +" = bt.indicators.Momentum" + "(period = " + str(options_listm[2]) + ")\n")
                            variable_name.append("self.Momentum" +number_mom)
                            number_macd1 = str(random.randint(17,19))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[3]) +",period_me2 =" + str(options_listm[4]) + ",period_signal =" + str(options_listm[5]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                        if indicator_listm[3] == 'SMA':
                            number_sma = str(random.randint(20,22))
                            number_macd1 = str(random.randint(20,22))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[3]) +",period_me2 =" + str(options_listm[4]) + ",period_signal =" + str(options_listm[5]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                            rule1.write("\t\tself.SMA "+ " = bt.indicators.MACD" + "(self.datas[0] , period =" + str(options_listm[5])+ ")\n")
                            variable_name.append("self.SMA" +number_sma)
                        
                        elif (indicator_listm[3] == 'RSI'):
                            number_rsi = str(random.randint(20,22))
                            number_macd1 = str(random.randint(20,22))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[3]) +",period_me2 =" + str(options_listm[4]) + ",period_signal =" + str(options_listm[5]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                            rule1.write("\t\tself.RSI" +" = bt.indicators.RSI" + "(period = " + str(options_listm[5]) + ")\n")
                            variable_name.append("self.RSI" +number_rsi)
                        elif (indicator_listm[3] == 'Momentum'):
                            number_mom = str(random.randint(20,22))
                            number_macd1 = str(random.randint(20,22))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[3]) +",period_me2 =" + str(options_listm[4]) + ",period_signal =" + str(options_listm[5]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                            rule1.write("\t\tself.Momentum" +" = bt.indicators.Momentum" + "(period = " + str(options_listm[5]) + ")\n")
                            variable_name.append("self.Momentum" +number_mom)
                    if (indicator_listm[0] == 'MACD' and indicator_listm[1] != 'MACD') or (indicator_listm[0] != 'MACD' and indicator_listm[1] == 'MACD'):
                        if indicator_listm[2] == 'SMA':
                            number_sma = str(random.randint(17,19))
                            rule1.write("\t\tself.SMA "+ " = bt.indicators.MACD" + "(self.datas[0] , period =" + str(options_listm[4])+ ")\n")
                            variable_name.append("self.SMA" +number_sma)
                            number_macd1 = str(random.randint(17,19))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[5]) +",period_me2 =" + str(options_listm[6]) + ",period_signal =" + str(options_listm[7]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                        elif (indicator_listm[2] == 'RSI'):
                            number_rsi = str(random.randint(17,19))
                            rule1.write("\t\tself.RSI" +" = bt.indicators.RSI" + "(period = " + str(options_listm[4]) + ")\n")
                            variable_name.append("self.SMA" +number_sma)
                            number_macd1 = str(random.randint(17,19))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[5]) +",period_me2 =" + str(options_listm[6]) + ",period_signal =" + str(options_listm[7]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                        elif (indicator_listm[2] == 'Momentum'):
                            number_mom = str(random.randint(17,19))
                            rule1.write("\t\tself.Momentum" +" = bt.indicators.Momentum" + "(period = " + str(options_listm[4]) + ")\n")
                            variable_name.append("self.Momentum" +number_mom)
                            number_macd1 = str(random.randint(17,19))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[5]) +",period_me2 =" + str(options_listm[6]) + ",period_signal =" + str(options_listm[7]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                        if indicator_listm[3] == 'SMA':
                            number_sma = str(random.randint(20,22))
                            number_macd1 = str(random.randint(20,22))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[4]) +",period_me2 =" + str(options_listm[5]) + ",period_signal =" + str(options_listm[6]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                            rule1.write("\t\tself.SMA "+ " = bt.indicators.MACD" + "(self.datas[0] , period =" + str(options_listm[7])+ ")\n")
                            variable_name.append("self.SMA" +number_sma)
                        elif (indicator_listm[3] == 'RSI'):
                            number_rsi = str(random.randint(20,22))
                            number_macd1 = str(random.randint(20,22))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[4]) +",period_me2 =" + str(options_listm[5]) + ",period_signal =" + str(options_listm[6]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                            rule1.write("\t\tself.RSI" +" = bt.indicators.RSI" + "(period = " + str(options_listm[7]) + ")\n")
                            variable_name.append("self.RSI" +number_rsi)
                        elif (indicator_listm[3] == 'Momentum'):
                            number_mom = str(random.randint(20,22))
                            number_macd1 = str(random.randint(20,22))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[4]) +",period_me2 =" + str(options_listm[5]) + ",period_signal =" + str(options_listm[6]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                            rule1.write("\t\tself.Momentum" +" = bt.indicators.Momentum" + "(period = " + str(options_listm[7]) + ")\n")
                            variable_name.append("self.Momentum" +number_mom)
                    if (indicator_listm[0] == 'MACD' and indicator_listm[1] == 'MACD'):
                        if indicator_listm[3] == 'SMA':
                            number_sma = str(random.randint(17,19))
                            rule1.write("\t\tself.SMA"+number_sma+ " = bt.indicators.MACD" + "(self.datas[0] , period =" + str(options_listm[6])+ ")\n")
                            variable_name.append("self.SMA" +number_sma)
                            number_macd1 = str(random.randint(17,19))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[7]) +",period_me2 =" + str(options_listm[8]) + ",period_signal =" + str(options_listm[9]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                        elif (indicator_listm[3] == 'RSI'):
                            number_rsi = str(random.randint(17,19))
                            rule1.write("\t\tself.RSI" +" = bt.indicators.RSI" + "(period = " + str(options_listm[6]) + ")\n")
                            variable_name.append("self.RSI" +number_rsi)
                            number_macd1 = str(random.randint(17,19))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[7]) +",period_me2 =" + str(options_listm[8]) + ",period_signal =" + str(options_listm[9]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
                        elif (indicator_listm[3] == 'Momentum'):
                            number_mom = str(random.randint(17,19))
                            rule1.write("\t\tself.Momentum" +" = bt.indicators.Momentum" + "(period = " + str(options_listm[6]) + ")\n")
                            variable_name.append("self.Momentum" +number_mom)
                            number_macd1 = str(random.randint(17,19))
                            rule1.write("\t\tself.MACD" +number_macd1+ " = bt.indicators.MACD" + "(self.data , period_me1 =" + str(options_listm[7]) +",period_me2 =" + str(options_listm[8]) + ",period_signal =" + str(options_listm[9]) + ")\n")
                            variable_name.append("self.MACD" +number_macd1)
            print(variable_name)
                
        else:#case where the length is 2
            print('length of options list : '+str(len(options_listm)))
            for item in options_listm:
                print(item)
            print(indicator_listm)
            option1 = options_list[0]
            option2 = options_list[1]
            rule1 = open('rule_writing.txt','a')
            if count ==0:
                if indicator_listm[0] == 'SMA': 
                    sma_number = str(random.randint(0,1))
                    rule1.write("\t\tself.SMA"+sma_number+ " = bt.indicators.SMA" + "(self.datas[0] , period =" + str(options_listm[0])+ ")\n") 
                    variable_name.append("self.SMA" +sma_number)
                elif (indicator_listm[0] == 'RSI'):
                    rsi_number = str(random.randint(0,1))
                    rule1.write("\t\tself.RSI" +rsi_number+" = bt.indicators.RSI" + "(period = " + str(options_listm[0]) + ")\n")
                    variable_name.append("self.RSI" +rsi_number)
                elif (indicator_listm[0] == 'Momentum'):
                    mom_number = str(random.randint(0,1))
                    rule1.write("\t\tself.Momentum" +mom_number+" = bt.indicators.Momentum" + "(period = " + str(options_listm[0]) + ")\n")   
                    variable_name.append("self.Momentum" +mom_number)
                if indicator_listm[1] == 'SMA': 
                    sma_number = str(random.randint(4,5))
                    rule1.write("\t\tself.SMA"+sma_number+ " = bt.indicators.SMA" + "(self.datas[0] , period =" + str(options_listm[1])+ ")\n")
                    variable_name.append("self.SMA" +sma_number)
                elif (indicator_listm[1] == 'RSI'):
                    rsi_number = str(random.randint(4,5))
                    rule1.write("\t\tself.RSI" +rsi_number+" = bt.indicators.RSI" + "(period = " + str(options_listm[1]) + ")\n")
                    variable_name.append("self.RSI" +rsi_number)
                elif (indicator_listm[1] == 'Momentum'):
                    mom_number = str(random.randint(4,5))
                    rule1.write("\t\tself.Momentum" +mom_number+" = bt.indicators.Momentum" + "(period = " + str(options_listm[1]) + ")\n")
                    variable_name.append("self.Momentum" +mom_number)
            
            if count == 1:
                if (indicator_listm[0] == 'MACD' and indicator_listm[1] == 'MACD'):
                    if indicator_listm[2] == 'SMA':
                        sma_number = str(random.randint(2,3))                
                        rule1.write("\t\tself.SMA"+sma_number+ " = bt.indicators.SMA" + "(self.datas[0] , period =" + str(options_listm[6])+ ")\n")
                        variable_name.append("self.SMA" +sma_number)
                    elif (indicator_listm[2] == 'RSI'):
                        rsi_number = str(random.randint(2,3))
                        rule1.write("\t\tself.RSI" +rsi_number+" = bt.indicators.RSI" + "(period = " + str(options_listm[6]) + ")\n")
                        variable_name.append("self.RSI" +rsi_number)
                    elif (indicator_listm[2] == 'Momentum'):
                        mom_number = str(random.randint(2,3))
                        rule1.write("\t\tself.Momentum" +mom_number+" = bt.indicators.Momentum" + "(period = " + str(options_listm[6]) + ")\n") 
                        variable_name.append("self.Momentum" +mom_number)
                    if indicator_listm[3] == 'SMA':
                        sma_number = str(random.randint(0,1))                
                        rule1.write("\t\tself.SMA"+sma_number+ " = bt.indicators.SMA" + "(self.datas[0] , period =" + str(options_listm[7])+ ")\n")
                        variable_name.append("self.SMA" +sma_number)
                    elif (indicator_listm[3] == 'RSI'):
                        rsi_number = str(random.randint(0,1))
                        rule1.write("\t\tself.RSI" +rsi_number+" = bt.indicators.RSI" + "(period = " + str(options_listm[7]) + ")\n")
                        variable_name.append("self.RSI" +rsi_number)
                    elif (indicator_listm[3] == 'Momentum'):
                        mom_number = str(random.randint(0,1))
                        rule1.write("\t\tself.Momentum" +mom_number+" = bt.indicators.Momentum" + "(period = " + str(options_listm[7]) + ")\n")     
                        variable_name.append("self.Momentum" +mom_number)
                
                if (indicator_listm[0] != 'MACD' and indicator_listm[1] == 'MACD') or (indicator_listm[0] == 'MACD' and indicator_listm[1] != 'MACD'):                         
                    if indicator_listm[2] == 'SMA':
                        sma_number = str(random.randint(0,1))                
                        rule1.write("\t\tself.SMA"+sma_number+ " = bt.indicators.SMA" + "(self.datas[0] , period =" + str(options_listm[4])+ ")\n")
                        variable_name.append("self.SMA" +sma_number)
                    elif (indicator_listm[2] == 'RSI'):
                        rsi_number = str(random.randint(0,1))
                        rule1.write("\t\tself.RSI" +rsi_number+" = bt.indicators.RSI" + "(period = " + str(options_listm[4]) + ")\n")
                        variable_name.append("self.RSI" +rsi_number)
                    elif (indicator_listm[2] == 'Momentum'):
                        mom_number = str(random.randint(0,1))
                        rule1.write("\t\tself.Momentum" +mom_number+" = bt.indicators.Momentum" + "(period = " + str(options_listm[4]) + ")\n")                 
                        variable_name.append("self.Momentum" +mom_number)
                    if indicator_listm[3] == 'SMA':
                        sma_number = str(random.randint(2,3))                
                        rule1.write("\t\tself.SMA"+sma_number+ " = bt.indicators.SMA" + "(self.datas[0] , period =" + str(options_listm[4])+ ")\n")  
                        variable_name.append("self.SMA" +sma_number)
                    elif (indicator_listm[3] == 'RSI'):
                        rsi_number = str(random.randint(2,3))
                        rule1.write("\t\tself.RSI" +rsi_number+" = bt.indicators.RSI" + "(period = " + str(options_listm[4]) + ")\n")
                        variable_name.append("self.RSI" +rsi_number)
                    elif (indicator_listm[3] == 'Momentum'):
                        mom_number = str(random.randint(2,3))
                        rule1.write("\t\tself.Momentum" +mom_number+" = bt.indicators.Momentum" + "(period = " + str(options_listm[4]) + ")\n")  
                        variable_name.append("self.Momentum" +mom_number)
                if (indicator_listm[0] != 'MACD' and indicator_listm[1] != 'MACD'):
                    if indicator_listm[2] == 'SMA':
                        sma_number = str(random.randint(0,1))                
                        rule1.write("\t\tself.SMA"+sma_number+ " = bt.indicators.SMA" + "(self.datas[0] , period =" + str(options_listm[2])+ ")\n")
                        variable_name.append("self.SMA" +sma_number)
                    elif (indicator_listm[2] == 'RSI'):
                        rsi_number = str(random.randint(0,1))
                        rule1.write("\t\tself.RSI" +rsi_number+" = bt.indicators.RSI" + "(period = " + str(options_listm[2]) + ")\n")
                        variable_name.append("self.RSI" +rsi_number)
                    elif (indicator_listm[2] == 'Momentum'):
                        mom_number = str(random.randint(0,1))
                        rule1.write("\t\tself.Momentum" +mom_number+" = bt.indicators.Momentum" + "(period = " + str(options_listm[2]) + ")\n")
                        variable_name.append("self.Momentum" +mom_number)
                    if indicator_listm[3] == 'SMA':
                        sma_number = str(random.randint(2,3))                
                        rule1.write("\t\tself.SMA"+sma_number+ " = bt.indicators.SMA" + "(self.datas[0] , period =" + str(options_listm[2])+ ")\n")  
                        variable_name.append("self.SMA" +sma_number)
                    elif (indicator_listm[3] == 'RSI'):
                        rsi_number = str(random.randint(2,3))
                        rule1.write("\t\tself.RSI" +rsi_number+" = bt.indicators.RSI" + "(period = " + str(options_listm[2]) + ")\n")
                        variable_name.append("self.RSI" +rsi_number)
                    elif (indicator_listm[3] == 'Momentum'):
                        mom_number = str(random.randint(2,3))
                        rule1.write("\t\tself.Momentum" +mom_number+" = bt.indicators.Momentum" + "(period = " + str(options_listm[2]) + ")\n")
                        variable_name.append("self.Momentum" +mom_number)
                
            print(variable_name)
            rule1.close()
        count = count + 1
            
    if number_indicators == 3:
        
        if comp_list[0] == 0:
            comp1 = '<'
        if comp_list[0] == 1:
            comp1 = '<='
        if comp_list[0] == 2:
            comp1 = '>'
        if comp_list[0] == 3:
            comp1 = '>='
        if comp_list[0] == 4:
            comp1 = '=='
        if comp_list[0] == 5:
            comp1 = '!='
            
        if comp_list[1] == 0:
            comp2 = '<'
        if comp_list[1] == 1:
            comp2 = '<='
        if comp_list[1] == 2:
            comp2 = '>'
        if comp_list[1] == 3:
            comp2 = '>='
        if comp_list[1] == 4:
            comp2 = '=='
        if comp_list[1] == 5:
            comp2 = '!='
            
        if comp_list[2] == 0:
            comp3 = '<'
        if comp_list[2] == 1:
            comp3 = '<='
        if comp_list[2] == 2:
            comp3 = '>'
        if comp_list[2] == 3:
            comp3 = '>='
        if comp_list[2] == 4:
            comp3 = '=='
        if comp_list[2] == 5:
            comp3 = '!='
        
        if log_op_list[0] == 0:
            first_logical_operator = 'and'
        else:
            first_logical_operator = 'or'
        if log_op_list[1] == 1:
            second_logical_operator = 'and'
        else:
            second_logical_operator = 'or'
            
        value1 = values_list[0]
        value2 = values_list[1]
        value3 = values_list[2]
        
        if len(options_list) == 9:
            option1_1 = options_list[0]
            option1_2 = options_list[1]
            option1_3 = options_list[2]
            option2_1 = options_list[3]
            option2_2 = options_list[4]
            option2_3 = options_list[5]
            option3_1 = options_list[6]
            option3_2 = options_list[7]
            option3_3 = options_list[8]
            rule1 = open('rule_writing.txt','w')
            rule1.write("if("+str(indicator_list[0]) + "("+ str(option1_1)+"'"+
                                 str(option1_2)+"'"+str(option1_3)+")"+
                                comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) + "("+ str(option2_1)+"'"+
                                 str(option2_2)+"'"+str(option2_3)+")" +comp2+str(value2)+
                                    str(second_logical_operator)+ str(indicator_list[2]) + 
                                    "("+ str(option3_1)+"'"+
                                 str(option3_2)+"'"+str(option3_3)+")" +comp3+str(value3)+
                                ") \n\tself."+order_type+"()")
            rule1.close()        
        
        elif len(options_list) == 7:
            if indicator_list[0] == 'MACD' and indicator_list[2] == 'MACD':  
                option1_1 = options_list[0]
                option1_2 = options_list[1]
                option1_3 = options_list[2]
                option2 = options_list[3]
                option3_1 = options_list[4]
                option3_2 = options_list[5]
                option3_3 = options_list[6]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1_1)+"'"+
                                 str(option1_2)+"'"+str(option1_3)+")"+
                                comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) + "("+ str(option2)+
                                 ")" +comp2+str(value2)+str(second_logical_operator)+
                                    str(indicator_list[2]) + 
                                    "("+ str(option3_1)+"'"+
                                 str(option3_2)+"'"+str(option3_3)+")" +comp3+str(value3)+
                                ") \n\tself."+order_type+"()")
                rule1.close()
                
            elif indicator_list[0] == 'MACD' and indicator_list[1] == 'MACD' :
                option1_1 = options_list[0]
                option1_2 = options_list[1]
                option1_3 = options_list[2]
                option2_1 = options_list[3]
                option2_2 = options_list[4]
                option2_3 = options_list[5]
                option3 = options_list[6]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1_1)+"'"+
                                 str(option1_2)+"'"+str(option1_3)+")"+
                                comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) + "("+ str(option2_1)+"'"+
                                 str(option2_2)+"'"+str(option2_3)+")"+
                                comp2 + str(value2)+str(second_logical_operator)+
                                    str(indicator_list[2]) + 
                                    "("+ str(option3)+")" +comp3+str(value3)+
                                ") \n\tself."+order_type+"()")
                rule1.close()
                
            elif indicator_list[1] == 'MACD' and indicator_list[2] == 'MACD' :
                option1 = options_list[0]
                option2_1 = options_list[1]
                option2_2 = options_list[2]
                option2_3 = options_list[3]
                option3_1 = options_list[4]
                option3_2 = options_list[5]
                option3_3 = options_list[6]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1)+")"+
                                comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) + "("+ str(option2_1)+"'"+
                                 str(option2_2)+"'"+str(option2_3)+")"+
                                comp2 + str(value2)+str(second_logical_operator)+
                                    str(indicator_list[2]) + "("+ str(option3_1)+"'"+
                                 str(option3_2)+"'"+str(option3_3)+")"+
                                comp3 + str(value3)+
                                ") \n\tself."+order_type+"()")
                rule1.close()
        if len(options_list) == 5:
            if indicator_list[0] == 'MACD':
                option1_1 = options_list[0]
                option1_2 = options_list[1]
                option1_3 = options_list[2]
                option2 = options_list[3]
                option3 = options_list[4]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1_1)+"'"+
                                 str(option1_2)+"'"+str(option1_3)+")"+
                                comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) +
                                "("+ str(option2) + ")" + comp2 + str(value2) +
                                str(second_logical_operator) + str(indicator_list[2])+
                                "(" + str(option3) + ")" +comp3 + str(value3) + ") \n\tself."+
                                    order_type+"()")
                rule1.close()
                                
                                
            if indicator_list[1] == 'MACD':
                option1 = options_list[0]
                option2_1 = options_list[1]
                option2_2 = options_list[2]
                option2_3 = options_list[3]
                option3 = options_list[4]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1)+
                                 ")"+
                                comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) +
                                "("+ str(option2_1)+"'"+
                                 str(option2_2)+"'"+str(option2_3) + ")" + comp2 + str(value2) +
                                str(second_logical_operator) + str(indicator_list[2])+
                                "(" + str(option3) + ")" +comp3 + str(value3) + ") \n\tself."+
                                    order_type+"()")
                rule1.close()
            else:
                option1 = options_list[0]
                option2 = options_list[1]
                option3_1 = options_list[2]
                option3_2 = options_list[3]
                option3_3 = options_list[4]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1)
                                 +")"+
                                comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) +
                                "("+ str(option2) + ")" + comp2 + str(value2) +
                                str(second_logical_operator) + str(indicator_list[2])+
                                "(" + str(option3_1)+"'"+
                                 str(option3_2)+"'"+str(option3_3) + ")" +comp3 + 
                                str(value3) + ") \n\tself."+
                                    order_type+"()")
                rule1.close()
                
        if len(options_list) == 3:
            option1 = options_list[0]
            option2 = options_list[1]
            option3 = options_list[2]
            rule1 = open('rule_writing.txt','w')
            rule1.write("if("+str(indicator_list[0]) + "("+str(option1)+")"+
                                comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) +
                                "("+ str(option2) + ")" + comp2 + str(value2) +
                                str(second_logical_operator) + str(indicator_list[2])+
                                "(" +str(option3) + ")" +comp3 + 
                                str(value3) + ") \n\tself."+
                                    order_type+"()")
            rule1.close()
            
    if number_indicators == 4:
        
        if comp_list[0] == 0:
            comp1 = '<'
        if comp_list[0] == 1:
            comp1 = '<='
        if comp_list[0] == 2:
            comp1 = '>'
        if comp_list[0] == 3:
            comp1 = '>='
        if comp_list[0] == 4:
            comp1 = '=='
        if comp_list[0] == 5:
            comp1 = '!='
            
        if comp_list[1] == 0:
            comp2 = '<'
        if comp_list[1] == 1:
            comp2 = '<='
        if comp_list[1] == 2:
            comp2 = '>'
        if comp_list[1] == 3:
            comp2 = '>='
        if comp_list[1] == 4:
            comp2 = '=='
        if comp_list[1] == 5:
            comp2 = '!='
            
        if comp_list[2] == 0:
            comp3 = '<'
        if comp_list[2] == 1:
            comp3 = '<='
        if comp_list[2] == 2:
            comp3 = '>'
        if comp_list[2] == 3:
            comp3 = '>='
        if comp_list[2] == 4:
            comp3 = '=='
        if comp_list[2] == 5:
            comp3 = '!='
        
        if comp_list[3] == 0:
            comp4 = '<'
        if comp_list[3] == 1:
            comp4 = '<='
        if comp_list[3] == 2:
            comp4 = '>'
        if comp_list[3] == 3:
            comp4 = '>='
        if comp_list[3] == 4:
            comp4 = '=='
        if comp_list[3] == 5:
            comp4 = '!='
            
            
        if log_op_list[0] == 0:
            first_logical_operator = 'and'
        else:
            first_logical_operator = 'or'
        if log_op_list[1] == 1:
            second_logical_operator = 'and'
        else:
            second_logical_operator = 'or'
        if log_op_list[2] == 2:
            third_logical_operator = 'and'
        else:
            third_logical_operator = 'or'
            
        value1 = values_list[0]
        value2 = values_list[1]
        value3 = values_list[2]
        value4 = values_list[3]
        
        if len(options_list) == 12:
            option1_1 = options_list[0]
            option1_2 = options_list[1]
            option1_3 = options_list[2]
            option2_1 = options_list[3]
            option2_2 = options_list[4]
            option2_3 = options_list[5]
            option3_1 = options_list[6]
            option3_2 = options_list[7]
            option3_3 = options_list[8]
            option4_1 = options_list[9]
            option4_2 = options_list[10]
            option4_3 = options_list[11]
            rule1 = open('rule_writing.txt','w')
            rule1.write("if("+str(indicator_list[0]) + "("+ str(option1_1)+"'"+
                                 str(option1_2)+"'"+str(option1_3)+")"+
                                comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) + "("+ str(option2_1)+"'"+
                                 str(option2_2)+"'"+str(option2_3)+")" +comp2+str(value2)+
                                    str(second_logical_operator)+ str(indicator_list[2]) + 
                                    "("+ str(option3_1)+"'"+
                                 str(option3_2)+"'"+str(option3_3)+")" +comp3+str(value3)+str(third_logical_operator)+ 
                                      str(indicator_list[3]) + 
                                    "("+ str(option4_1)+"'"+
                                 str(option4_2)+"'"+str(option4_3)+")" +comp4+str(value4)+
                                ") \n\tself."+order_type+"()")
            rule1.close()        
        
        elif len(options_list) == 10:
            if indicator_list[0] == 'MACD' and indicator_list[1] == 'MACD' and indicator_list[2] == 'MACD':  
                option1_1 = options_list[0]
                option1_2 = options_list[1]
                option1_3 = options_list[2]
                option2_1 = options_list[3]
                option2_2 = options_list[4]
                option2_3 = options_list[5]
                option3_1 = options_list[6]
                option3_2 = options_list[7]
                option3_3 = options_list[8]
                option4 = options_list[9]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1_1)+"'"+
                                 str(option1_2)+"'"+str(option1_3)+")"+
                                comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) + "("+ str(option2_1)+"'"+
                                 str(option2_2)+"'"+str(option2_3)+")" +comp2+str(value2)+
                                    str(second_logical_operator)+ str(indicator_list[2]) + 
                                    "("+ str(option3_1)+"'"+
                                 str(option3_2)+"'"+str(option3_3)+")" +comp3+str(value3)+str(third_logical_operator)+
                                    str(indicator_list[3]) + 
                                    "("+ str(option4)+")"+comp4+str(value4)+
                                ") \n\tself."+order_type+"()")
                rule1.close()
                
            elif indicator_list[0] == 'MACD' and indicator_list[1] == 'MACD' and indicator_list[3] == 'MACD':  
                option1_1 = options_list[0]
                option1_2 = options_list[1]
                option1_3 = options_list[2]
                option2_1 = options_list[3]
                option2_2 = options_list[4]
                option2_3 = options_list[5]
                option3 = options_list[6]
                option4_1 = options_list[7]
                option4_2 = options_list[8]
                option4_3 = options_list[9]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1_1)+"'"+
                                 str(option1_2)+"'"+str(option1_3)+")"+
                                comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) + "("+ str(option2_1)+"'"+
                                 str(option2_2)+"'"+str(option2_3)+")" +comp2+str(value2)+
                                    str(second_logical_operator)+ str(indicator_list[2]) + 
                                    "("+ str(option3)+")" +comp3+str(value3)+str(third_logical_operator)+
                                    str(indicator_list[3]) + 
                                    "("+ str(option4_1)+"'"+
                                 str(option4_2)+"'"+str(option4_3)+")"+comp4+str(value4)+
                                ") \n\tself."+order_type+"()")
                rule1.close()
                
            elif indicator_list[0] == 'MACD' and indicator_list[2] == 'MACD' and indicator_list[3] == 'MACD':  
                option1_1 = options_list[0]
                option1_2 = options_list[1]
                option1_3 = options_list[2]
                option2 = options_list[3]
                option3_1 = options_list[4]
                option3_2 = options_list[5]
                option3_3 = options_list[6]
                option4_1 = options_list[7]
                option4_2 = options_list[8]
                option4_3 = options_list[9]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1_1)+"'"+
                                 str(option1_2)+"'"+str(option1_3)+")"+
                                comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) + "("+ str(option2)+")" +comp2+str(value2)+
                                    str(second_logical_operator)+ str(indicator_list[2]) + 
                                    "("+ str(option3_1)+"'"+
                                 str(option3_2)+"'"+str(option3_3)+")" +comp3+str(value3)+str(third_logical_operator)+
                                    str(indicator_list[3]) + 
                                    "("+ str(option4_1)+"'"+
                                 str(option4_2)+"'"+str(option4_3)+")"+comp4+str(value4)+
                                ") \n\tself."+order_type+"()")
                rule1.close()
                
            elif indicator_list[0] == 'MACD' and indicator_list[2] == 'MACD' and indicator_list[3] == 'MACD':  
                option1_1 = options_list[0]
                option1_2 = options_list[1]
                option1_3 = options_list[2]
                option2 = options_list[3]
                option3_1 = options_list[4]
                option3_2 = options_list[5]
                option3_3 = options_list[6]
                option4_1 = options_list[7]
                option4_2 = options_list[8]
                option4_3 = options_list[9]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1_1)+"'"+
                                 str(option1_2)+"'"+str(option1_3)+")"+
                                comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) + "("+str(option2)+")" +comp2+str(value2)+
                                    str(second_logical_operator)+ str(indicator_list[2]) + 
                                    "("+ str(option3_1)+"'"+
                                 str(option3_2)+"'"+str(option3_3)+")" +comp3+str(value3)+str(third_logical_operator)+
                                    str(indicator_list[3]) + 
                                    "("+ str(option4_1)+"'"+
                                 str(option4_2)+"'"+str(option4_3)+")"+comp4+str(value4)+
                                ") \n\tself."+order_type+"()")
                rule1.close()
                
        if len(options_list) == 8:
            if indicator_list[0] == 'MACD'and indicator_list[1] == 'MACD':
                option1_1 = options_list[0]
                option1_2 = options_list[1]
                option1_3 = options_list[2]
                option2_1 = options_list[3]
                option2_2 = options_list[4]
                option2_3 = options_list[5]
                option3 = options_list[6]
                option4 = options_list[7]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1_1)+"'"+
                                 str(option1_2)+"'"+str(option1_3)+")"+
                                comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) + "("+ str(option2_1)+"'"+
                                 str(option2_2)+"'"+str(option2_3)+")" +comp2+str(value2)+
                                    str(second_logical_operator)+ str(indicator_list[2]) + 
                                    "("+ str(option3)+")" +comp3+str(value3)+str(third_logical_operator)+
                                    str(indicator_list[3]) + 
                                    "("+ str(option4)+")"+comp4+str(value4)+
                                ") \n\tself."+order_type+"()")
                rule1.close()
        
            elif indicator_list[0] == 'MACD'and indicator_list[2] == 'MACD':
                option1_1 = options_list[0]
                option1_2 = options_list[1]
                option1_3 = options_list[2]
                option2 = options_list[3]
                option3_1 = options_list[4]
                option3_2 = options_list[5]
                option3_3 = options_list[6]
                option4 = options_list[7]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1_1)+"'"+
                                 str(option1_2)+"'"+str(option1_3)+")"+
                                comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) + "("+ str(option2)+")" +comp2+str(value2)+
                                    str(second_logical_operator)+ str(indicator_list[2]) + 
                                    "("+ str(option3_1)+"'"+
                                 str(option3_2)+"'"+str(option3_3)+")" +comp3+str(value3)+str(third_logical_operator)+
                                    str(indicator_list[3]) + 
                                    "("+ str(option4)+")"+comp4+str(value4)+
                                ") \n\tself."+order_type+"()")
                rule1.close()
                
            elif indicator_list[0] == 'MACD'and indicator_list[3] == 'MACD':
                option1_1 = options_list[0]
                option1_2 = options_list[1]
                option1_3 = options_list[2]
                option2 = options_list[3]
                option3 = options_list[4]
                option4_1 = options_list[5]
                option4_2 = options_list[6]
                option4_3 = options_list[7]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1_1)+"'"+
                                 str(option1_2)+"'"+str(option1_3)+")"+
                                comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) + "("+ str(option2)+")" +comp2+str(value2)+
                                    str(second_logical_operator)+ str(indicator_list[2]) + 
                                    "("+ str(option3)+")" +comp3+str(value3)+str(third_logical_operator)+
                                    str(indicator_list[3]) + 
                                    "("+ str(option4_1)+"'"+
                                 str(option4_2)+"'"+str(option4_3)+")"+comp4+str(value4)+
                                ") \n\tself."+order_type+"()")
                rule1.close()
        
        
        
        if len(options_list) == 8:
            if indicator_list[1] == 'MACD' and indicator_list[2] == 'MACD':
                option1 = options_list[0]
                option2_1 = options_list[1]
                option2_2 = options_list[2]
                option2_3 = options_list[3]
                option3_1 = options_list[4]
                option3_2 = options_list[5]
                option3_3 = options_list[6]
                option4 = options_list[7]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1)+ ")"                           
                                +comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) +
                                "("+ str(option2_1)+"'"+
                                 str(option2_2)+"'"+str(option2_3) + ")" + comp2 + str(value2) +
                                str(second_logical_operator) + str(indicator_list[2])+
                                "(" + str(option3_1)+"'"+
                                 str(option3_2)+"'"+str(option3_3) + ")" +comp3 + 
                                str(value3) + str(third_logical_operator)+ str(indicator_list[3])+
                                "(" + str(option4) + ")" + comp4 + str(value4) +
                                ") \n\tself."+
                                    order_type+"()")
                                
                        
                rule1.close()
            
            if indicator_list[1] == 'MACD' and  indicator_list[3] == 'MACD':
                option1 = options_list[0]
                option2_1 = options_list[1]
                option2_2 = options_list[2]
                option2_3 = options_list[3]
                option3 = options_list[4]
                option4_1 = options_list[5]
                option4_2 = options_list[6]
                option4_3 = options_list[7]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1)+ ")"                           
                                +comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) +
                                "("+ str(option2_1)+"'"+
                                 str(option2_2)+"'"+str(option2_3) + ")" + comp2 + str(value2) +
                                str(second_logical_operator) + str(indicator_list[2])+
                                "(" +
                                 str(option3)+")" +comp3 + 
                                str(value3) + str(third_logical_operator)+ str(indicator_list[3])+
                                "(" + str(option4_1)+"'"+
                                 str(option4_2)+"'"+str(option4_3) + ")" + comp4 + str(value4) +
                                ") \n\tself."+
                                    order_type+"()")
                rule1.close()
                
            if indicator_list[2] == 'MACD' and  indicator_list[3] == 'MACD':
                option1 = options_list[0]
                option2 = options_list[1]
                option3_1 = options_list[2]
                option3_2 = options_list[3]
                option3_3 = options_list[4]
                option4_1 = options_list[5]
                option4_2 = options_list[6]
                option4_3 = options_list[7]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1)+ ")"                           
                                +comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) +
                                "("+str(option2) + ")" + comp2 + str(value2) +
                                str(second_logical_operator) + str(indicator_list[2])+
                                "(" + str(option3_1)+"'"+
                                 str(option3_2)+"'"+str(option3_3)
                                 +")" +comp3 + 
                                str(value3) + str(third_logical_operator)+ str(indicator_list[3])+
                                "(" + str(option4_1)+"'"+
                                 str(option4_2)+"'"+str(option4_3) + ")" + comp4 + str(value4) +
                                ") \n\tself."+
                                    order_type+"()")
                rule1.close()
                
        if len(options_list) == 6:
            if indicator_list[0] == 'MACD':
                option1_1 = options_list[0]
                option1_2 = options_list[1]
                option1_3 = options_list[2]
                option2 = options_list[3]
                option3 = options_list[4]
                option4 = options_list[7]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1_1)+"'"+
                                 str(option1_2)+"'"+str(option1_3)+ ")"                           
                                +comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) +
                                "("+ str(option2) + ")" + comp2 + str(value2) +
                                str(second_logical_operator) + str(indicator_list[2])+
                                "(" + str(option3) + ")" +comp3 + 
                                str(value3) + str(third_logical_operator)+ str(indicator_list[3])+
                                "(" + str(option4) + ")" + comp4 + str(value4) +
                                ") \n\tself."+
                                    order_type+"()")
                                
                        
                rule1.close()
            
            if indicator_list[1] == 'MACD':
                option1 = options_list[0]
                option2_1 = options_list[1]
                option2_2 = options_list[2]
                option2_3 = options_list[3]
                option3 = options_list[4]
                option4 = options_list[5]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1)+ ")"                           
                                +comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) +
                                "("+ str(option2_1)+"'"+
                                 str(option2_2)+"'"+str(option2_3) + ")" + comp2 + str(value2) +
                                str(second_logical_operator) + str(indicator_list[2])+
                                "(" +
                                 str(option3)+")" +comp3 + 
                                str(value3) + str(third_logical_operator)+ str(indicator_list[3])+
                                "(" + str(option4)+ ")" + comp4 + str(value4) +
                                ") \n\tself."+
                                    order_type+"()")
                rule1.close()
                
            if indicator_list[2] == 'MACD':
                option1 = options_list[0]
                option2 = options_list[1]
                option3_1 = options_list[2]
                option3_2 = options_list[3]
                option3_3 = options_list[4]
                option4 = options_list[5]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1)+ ")"                           
                                +comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) +
                                "("+str(option2) + ")" + comp2 + str(value2) +
                                str(second_logical_operator) + str(indicator_list[2])+
                                "(" + str(option3_1)+"'"+
                                 str(option3_2)+"'"+str(option3_3)
                                 +")" +comp3 + 
                                str(value3) + str(third_logical_operator)+ str(indicator_list[3])+
                                "(" + str(option4)
                                  + ")" + comp4 + str(value4) +
                                ") \n\tself."+
                                    order_type+"()")
                rule1.close()
                
            if indicator_list[3] == 'MACD':
                option1 = options_list[0]
                option2 = options_list[1]
                option3 = options_list[2]
                option4_1 = options_list[3]
                option4_2 = options_list[4]
                option4_3 = options_list[5]
                rule1 = open('rule_writing.txt','w')
                rule1.write("if("+str(indicator_list[0]) + "("+ str(option1)+ ")"                           
                                +comp1 + str(value1) + str(first_logical_operator)+
                                str(indicator_list[1]) +
                                "("+str(option2) + ")" + comp2 + str(value2) +
                                str(second_logical_operator) + str(indicator_list[2])+
                                "(" + str(option3)+
                                 +")" +comp3 + 
                                str(value3) + str(third_logical_operator)+ str(indicator_list[3])+
                                "(" + str(option4_1)+"'"+
                                 str(option4_2)+"'"+str(option4_3)
                                  + ")" + comp4 + str(value4) +
                                ") \n\tself."+
                                    order_type+"()")
                rule1.close()
                    
        if len(options_list) == 4:
            option1 = options_list[0]
            option2 = options_list[1]
            option3 = options_list[2]
            option4 = options_list[3]
            rule1 = open('rule_writing.txt','w')
            rule1.write("if("+str(indicator_list[0]) + "("+ str(option1)+ ")"                           
                            +comp1 + str(value1) + str(first_logical_operator)+
                            str(indicator_list[1]) +
                            "("+str(option2) + ")" + comp2 + str(value2) +
                            str(second_logical_operator) + str(indicator_list[2])+
                            "(" + str(option3)                              
                             +")" +comp3 + 
                            str(value3) + str(third_logical_operator)+ str(indicator_list[3])+
                            "(" + str(option4)                                
                              + ")" + comp4 + str(value4) +
                            ") \n\tself."+
                                order_type+"()")
            rule1.close()
#    count = count + 1
                
                
                
            
            
            
        
        
#example = create_rule()
#test = create_member()
#pr++int(test[1])
#print(test[1])
#write_in_python_file(test[1], test[1][0])

#test = open('test_external.py','w')
#test.write("def f():\n\tprint(1)")
#test.close()
#import test_external#so simple, and yet so powerful ! ! ! ! :D
#test_external.f()

#generate population of random members
#1 member = 2 rules
#append the rules to the backtesting part
#backtest each member on the same period and same currency
#score each member based on the backtesting
#while some condition:
    #create a mating pool : repeat each member the number of times its score
    #do crossover and mutation on the pool
    #score each member


def mutate (mem):
    SMA_range_options = [10,30,50,70,90,110,130]
    SMA_range_values = ['SMA(10)','SMA(30)','SMA(50)','SMA(70)','SMA(90)','SMA(110)','SMA(130)','self.dataopen[-1]','self.datahigh[-1]','self.datalow[-1]','self.dataclose[-1]']

    
    MACD_range_options_EMA_fast = [5,15]
    MACD_range_options_EMA_slow = [20,30]
    MACD_range_options_SMA = [5,25]
    MACD_range_values = 0
    
    RSI_range_options = [10,20,30,40,50]
    RSI_range_values = random.randint(0,100)
    

    Momentum_range_options = random.randint(10,20)
    Momentum_range_values = round(random.uniform(92.48,109.81),2)
    
    list_indicators = [0,1,2,3]# 0=> SMA , 1=> MACD, 2=>RSI, 3=>Momentum
    list_comparators = [0,1,2,3,4,5]# 0<, 1<=, 2>, 3>=, 4==, 5!=
    list_logical = [0,1] # 0 and, 1 or
    list_orders = [0,1]# 0 => sell, 1 => buy

#    mem = create_member()
    global mut_rate
    mutation_rate = 0.05
    if mem[0][0] == 2:
        i=0
        while(i<len(mem[0])):
            rand = round(random.uniform(0,1),2)            
            if rand < 0.99:
#                mutate
                if i == 1:
                    print(rand)
                    old_indicator = mem[0][1]
                    new_indicator = random.randint(0,3)
                    if old_indicator == 1 and new_indicator != 1:
                        part1 =[mem[0][0],new_indicator,mem[0][2]]
                        if new_indicator == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option,new_sma_value ]
                        if new_indicator == 2:
                            new_rsi_value = RSI_range_values
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option,new_rsi_value ]
                        if new_indicator == 3:
                            new_mom_value = Momentum_range_values
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option,new_mom_value ]
                        part3 = mem[0][7:]
                        mem[0] = part1 + part2 + part3
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))

                    if old_indicator != 1 and new_indicator == 1:
                        part1 = [mem[0][0],new_indicator,mem[0][2]]
                        new_macd_value = 0
                        new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                        new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                        new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                        part2 = [new_macd_option_ema_slow,new_macd_option_ema_fast,new_macd_option_sma,new_macd_value]                    
                        part3 = mem[0][5:]
                        mem[0]= part1 + part2 + part3
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                        
                    if old_indicator == 1 and new_indicator == 1:
                        part1 = [mem[0][0],new_indicator,mem[0][2]]
                        new_macd_value = 0
                        new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                        new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                        new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                        part2 = [new_macd_option_ema_slow,new_macd_option_ema_fast,new_macd_option_sma,new_macd_value]
                        part3 = mem[0][7:]
                        mem[0]= part1 + part2 + part3
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                        
                    if old_indicator != 1 and new_indicator != 1:
                        part1 = [mem[0][0],new_indicator,mem[0][2]]
                        if new_indicator == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option,new_sma_value ]
                        if new_indicator == 2:
                            new_rsi_value = RSI_range_values
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option,new_rsi_value ]
                        if new_indicator == 3:
                            new_mom_value = Momentum_range_values
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option,new_mom_value ]
                        part3 = mem[0][5:]
                        mem[0]= part1 + part2 + part3
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                        
#                        first indicator not MACD
                if i == 2:
#                    print('i = ' + str(i) + ' random = ' + str(rand))
                    old_indicator = mem[0][2]
                    new_indicator = random.randint(0,3)
                    if mem[0][1] != 1:
                        if old_indicator == 1 and new_indicator != 1:
                            part1 = [mem[0][0],mem[0][1],new_indicator,mem[0][3],mem[0][4]]
                            if new_indicator == 0:
                                new_sma_value = SMA_range_values[random.randint(0,10)]
                                new_sma_option = SMA_range_options[random.randint(0,6)]
                                part2 = [new_sma_option,new_sma_value ]
                            if new_indicator == 2:
                                new_rsi_value = RSI_range_values
                                new_rsi_option = RSI_range_options[random.randint(0,4)]
                                part2 = [new_rsi_option,new_rsi_value ]
                            if new_indicator == 3:
                                new_mom_value = Momentum_range_values
                                new_mom_option = Momentum_range_options
                                part2 = [new_mom_option,new_mom_value ]
                            part3 = mem[0][9:]
                            mem[0] = part1 + part2 + part3
                            print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                            
                        
                        if old_indicator != 1 and new_indicator == 1:
                            part1 = [mem[0][0],mem[0][1],new_indicator,mem[0][3],mem[0][4]]
                            new_macd_value = 0
                            new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                            new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                            new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                            part2 = [new_macd_option_ema_slow,new_macd_option_ema_fast,new_macd_option_sma,new_macd_value]                                           
                            part3 = mem[0][7:]
                            mem[0]= part1 + part2 + part3
                            print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                            
                        if old_indicator == 1 and new_indicator == 1:
                            part1 = [mem[0][0],mem[0][1],new_indicator,mem[0][3],mem[0][4]]
                            new_macd_value = 0
                            new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                            new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                            new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                            part2 = [new_macd_option_ema_slow,new_macd_option_ema_fast,new_macd_option_sma,new_macd_value]                                          
                            part3 = mem[0][9:]
                            mem[0]= part1 + part2 + part3
                            print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                            
                        if old_indicator != 1 and new_indicator != 1:
                            part1 = [mem[0][0],mem[0][1],new_indicator,mem[0][3],mem[0][4]]
                            if new_indicator == 0:
                                new_sma_value = SMA_range_values[random.randint(0,10)]
                                new_sma_option = SMA_range_options[random.randint(0,6)]
                                part2 = [new_sma_option,new_sma_value ]
                            if new_indicator == 2:
                                new_rsi_value = RSI_range_values
                                new_rsi_option = RSI_range_options[random.randint(0,4)]
                                part2 = [new_rsi_option,new_rsi_value ]
                            if new_indicator == 3:
                                new_mom_value = Momentum_range_values
                                new_mom_option = Momentum_range_options
                                part2 = [new_mom_option,new_mom_value ]
                            part3 = mem[0][7:]
                            mem[0]= part1 + part2 + part3
                            print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                            
#                        first indicator is MACD
                    else:
                        
                        if old_indicator == 1 and new_indicator != 1:
                            part1 = [mem[0][0],mem[0][1],new_indicator,mem[0][3],mem[0][4],mem[0][5],mem[0][6]]
                            if new_indicator == 0:
                                new_sma_value = SMA_range_values[random.randint(0,10)]
                                new_sma_option = SMA_range_options[random.randint(0,6)]
                                part2 = [new_sma_option,new_sma_value ]
                            if new_indicator == 2:
                                new_rsi_value = RSI_range_values
                                new_rsi_option = RSI_range_options[random.randint(0,4)]
                                part2 = [new_rsi_option,new_rsi_value ]
                            if new_indicator == 3:
                                new_mom_value = Momentum_range_values
                                new_mom_option = Momentum_range_options
                                part2 = [new_mom_option,new_mom_value ]
                            part3 = mem[0][9:]
                            mem[0] = part1 + part2 + part3
                            print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                            
                        if old_indicator != 1 and new_indicator == 1:
                            part1 = [mem[0][0],mem[0][1],new_indicator,mem[0][3],mem[0][4],mem[0][5],mem[0][6]]
                            new_macd_value = 0
                            new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                            new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                            new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                            part2 = [new_macd_option_ema_slow,new_macd_option_ema_fast,new_macd_option_sma,new_macd_value]
                            part3 = mem[0][7:]
                            mem[0]= part1 + part2 + part3
                            print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                            
                        if old_indicator == 1 and new_indicator == 1:
                            part1 = [mem[0][0],mem[0][1],new_indicator,mem[0][3],mem[0][4],mem[0][5],mem[0][6]]
                            new_macd_value = 0
                            new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                            new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                            new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                            part2 = [new_macd_option_ema_slow,new_macd_option_ema_fast,new_macd_option_sma,new_macd_value]
                            part3 = mem[0][9:]
                            mem[0]= part1 + part2 + part3
                            print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                            
                        if old_indicator != 1 and new_indicator != 1:
                            part1 = [mem[0][0],mem[0][1],new_indicator,mem[0][3],mem[0][4],mem[0][5],mem[0][6]]
                            if new_indicator == 0:
                                new_sma_value = SMA_range_values[random.randint(0,10)]
                                new_sma_option = SMA_range_options[random.randint(0,6)]
                                part2 = [new_sma_option,new_sma_value ]
                            if new_indicator == 2:
                                new_rsi_value = RSI_range_values
                                new_rsi_option = RSI_range_options[random.randint(0,4)]
                                part2 = [new_rsi_option,new_rsi_value ]
                            if new_indicator == 3:
                                new_mom_value = Momentum_range_values
                                new_mom_option = Momentum_range_options
                                part2 = [new_mom_option,new_mom_value ]
                            part3 = mem[0][7:]
                            mem[0]= part1 + part2 + part3
                            print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                            
                            
               
                if i == 3:
                    part1 = [mem[0][0],mem[0][1],mem[0][2]]
                    if mem[0][1] == 0:
                        new_sma_option = SMA_range_options[random.randint(0,6)]
                        part2 = [new_sma_option]
                        part3 = mem[0][4:]
                    if mem[0][1] == 1:
                        new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                        part2 = [new_macd_option_ema_slow]
                        part3 = mem[0][4:]
                    if mem[0][1] == 2:
                        new_rsi_option = RSI_range_options[random.randint(0,4)]
                        part2 = [new_rsi_option]
                        part3 = mem[0][4:]
                    if mem[0][1] == 3:
                        new_mom_option = Momentum_range_options
                        part2 = [new_mom_option]
                        part3 = mem[0][4:]
                    mem[0] = part1 + part2 + part3
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    
                    
                if i == 4:
                    part1 = mem[0][:4]
                    if mem[0][1] == 0:                   
                        new_sma_value = SMA_range_values[random.randint(0,10)]
                        part2 = [new_sma_value]
                        part3 = mem[0][5:]
                    if mem[0][1] == 1:
                        new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                        part2 = [new_macd_option_ema_fast]
                        part3 = mem[0][5:]
                    if mem[0][1] == 2:
                        new_rsi_value = RSI_range_values
                        part2 = [new_rsi_value]
                        part3 = mem[0][5:]
                    if mem[0][1] == 3:
                        new_mom_value = Momentum_range_values
                        part2 = [new_mom_value]
                        part3 = mem[0][5:]
                    mem[0] = part1 + part2 + part3   
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    
          
                if i == 5:
                    part1 = mem[0][:5]
                    if mem[0][2] == 0:
                        new_sma_option = SMA_range_options[random.randint(0,6)]
                        part2 = [new_sma_option]
                        part3 = mem[0][6:]
                    if mem[0][2] == 1:
                        new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                        part2 = [new_macd_option_sma]
                        part3 = mem[0][6:]
                    if mem[0][2] == 2:
                        new_rsi_option = RSI_range_options[random.randint(0,4)]
                        part2 = [new_rsi_option]
                        part3 = mem[0][6:]
                    if mem[0][2] == 3:
                        new_mom_option = Momentum_range_options
                        part2 = [new_mom_option]
                        part3 = mem[0][6:]
                    mem[0] = part1 + part2 + part3
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    
                    
                if i == 6:
                    part1 = mem[0][:6]
                    if mem[0][1] != 1 and mem[0][2] == 1:
                        new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                        part2 = [new_macd_option_ema_fast]
                        part3 = mem[0][7:]
                    if mem[0][2] == 0:                   
                        new_sma_value = SMA_range_values[random.randint(0,10)]
                        part2 = [new_sma_value]
                        part3 = mem[0][7:]
                    if mem[0][1] == 1:
                        new_macd_value = 0
                        part2 = [new_macd_value]
                        part3 = mem[0][7:]
                    if mem[0][1] == 1 and mem[0][2] == 1:
                        new_macd_value = 0
                        part2 = [new_macd_value]
                        part3 = mem[0][7:]
                    if mem[0][1] == 1 and mem[0][2] != 1:
                        new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                        part2 = [new_macd_option_ema_fast]
                        part3 = mem[0][7:]
                    if mem[0][1] != 1 and mem[0][2] != 1:
                        if mem[0][2] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][7:]     
                        if mem[0][2] == 2:
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][7:]
                        if mem[0][3] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][7:]
                    if mem[0][2] == 2:
                        new_rsi_value = RSI_range_values
                        part2 = [new_rsi_value]
                        part3 = mem[0][7:]
                    if mem[0][2] == 3:
                        new_mom_value = Momentum_range_values
                        part2 = [new_mom_value]
                        part3 = mem[0][7:]
                    mem[0] = part1 + part2 + part3   
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    
                    
                if i == 7:
                    part1 = mem[0][:7]
                    if mem[0][1] == 1 and mem[0][2] == 1:
                        new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                        part2 = [new_macd_option_ema_slow]
                        part3 = mem[0][8:]
                    if mem[0][1] == 1 and mem[0][2] != 1:
                        if mem[0][2] == 0:
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option]
                            part3 = mem[0][8:]     
                        if mem[0][2] == 2:
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option]
                            part3 = mem[0][8:]
                        if mem[0][2] == 3:
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option]
                            part3 = mem[0][8:]
                    if mem[0][1] != 1 and mem[0][2] == 1:
                        new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                        part2 = [new_macd_option_sma]
                        part3 = mem[0][8:]
                    if mem[0][1] != 1 and mem[0][2] != 1:
                        new_comp = list_comparators[random.randint(0,5)]
                        part2 = [new_comp]
                        part3 = mem[0][8:]
                    mem[0] = part1 + part2 + part3
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    

                if i == 8:
                    part1 = mem[0][:8]
                    if mem[0][1] == 1 and mem[0][2] == 1:
                        new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                        part2 = [new_macd_option_ema_fast]
                        part3 = mem[0][9:]
                    elif mem[0][1] == 1 and mem[0][2] != 1:
                        if mem[0][2] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][9:]     
                        if mem[0][2] == 2:
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][9:]
                        if mem[0][2] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][9:]
                    elif mem[0][1] != 1 and mem[0][2] == 1:
                        new_macd_value = 0
                        part2 = [new_macd_value]
                        part3 = mem[0][9:]
                    elif mem[0][1] != 1 and mem[0][2] != 1:
                        new_comp = list_comparators[random.randint(0,5)]
                        part2 = [new_comp]
                        part3 = mem[0][9:]
                    mem[0] = part1 + part2 + part3 
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    

                if i == 9:
                    part1 = mem[0][:9]
                    if mem[0][1] == 1 and mem[0][2] == 1:
                        new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                        part2 = [new_macd_option_sma]
                        part3 = mem[0][10:]
                    elif mem[0][1] == 1 and mem[0][2] != 1:
                        new_comp = list_comparators[random.randint(0,5)]
                        part2 = [new_comp]
                        part3 = mem[0][10:]
                    elif mem[0][1] != 1 and mem[0][2] == 1:
                        new_comp = list_comparators[random.randint(0,5)]
                        part2 = [new_comp]
                        part3 = mem[0][10:]
                    elif mem[0][1] != 1 and mem[0][2] != 1:
                        new_logical = random.randint(0,1)
                        part2 = [new_logical]
                        part3 = mem[0][10:]
                    mem[0] = part1 + part2 + part3 
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    

                if i == 10:
                    part1 = mem[0][:10]
                    if mem[0][1] == 1 and mem[0][2] == 1:
                        new_macd_value = 0
                        part2 = [new_macd_value]
                        part3 = mem[0][11:]
                    elif mem[0][1] == 1 and mem[0][2] != 1:
                        new_comp = list_comparators[random.randint(0,5)]
                        part2 = [new_comp]
                        part3 = mem[0][11:]
                    elif mem[0][1] != 1 and mem[0][2] == 1:
                        new_comp = list_comparators[random.randint(0,5)]
                        part2 = [new_comp]
                        part3 = mem[0][11:]
                    elif mem[0][1] != 1 and mem[0][2] != 1:
                        new_order = random.randint(0,1)
                        if new_order == mem[1][-1]:
                            if new_order == 1:
                                mem[1][-1] = 0
                            else:
                                mem[1][-1] = 1
                        part2 = [new_order]
                        part3 = mem[0][11:]
                    mem[0] = part1 + part2 + part3  
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    

                if len(mem[0]) == 15:
                    if i == 11:
                        part1 = mem[0][:11]
                        if mem[0][1] == 1 and mem[0][2] == 1:
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][12:]
                        elif mem[0][1] == 1 and mem[0][2] != 1:
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][12:]
                        elif mem[0][1] != 1 and mem[0][2] == 1:
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][12:]                     
                        mem[0] = part1 + part2 + part3  
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                        
                        
                    if i == 12:
                        part1 = mem[0][:12]
                        if mem[0][1] == 1 and mem[0][2] == 1:
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][13:]
                        elif mem[0][1] == 1 and mem[0][2] != 1:
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]  
                        elif mem[0][1] != 1 and mem[0][2] == 1:
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]                
                        mem[0] = part1 + part2 + part3 
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                        
                    
                    if i == 13:
                        part1 = mem[0][:13]
                        if mem[0][1] == 1 and mem[0][2] == 1:
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][14:]
                        mem[0] = part1 + part2 + part3   
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                        
                    
                    if i == 14:
                        part1 = mem[0][:14]
                        if mem[0][1] == 1 and mem[0][2] == 1:
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]
                        mem[0] = part1 + part2 + part3 
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                        

                if len(mem[0]) == 13:
                    if i == 11:
                        part1 = mem[0][:11]
                        if mem[0][1] == 1 and mem[0][2] == 1:
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][12:]
                        elif mem[0][1] == 1 and mem[0][2] != 1:
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][12:]
                        elif mem[0][1] != 1 and mem[0][2] == 1:
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][12:]                     
                        mem[0] = part1 + part2 + part3  
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                        
                        
                    if i == 12:
                        part1 = mem[0][:12]
                        if mem[0][1] == 1 and mem[0][2] == 1:
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][13:]
                        elif mem[0][1] == 1 and mem[0][2] != 1:
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]  
                        elif mem[0][1] != 1 and mem[0][2] == 1:
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]                 
                        mem[0] = part1 + part2 + part3  
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))

            i = i + 1
    #########PART WITH 3 INDICATORS#######        
    if mem[0][0] == 3:
        i=0
        while(i<len(mem[0])):
            rand = round (random.uniform(0,1),2)
            if rand < 0.5:
                #mutate

                if i == 4:
                    part1 = mem[0][:i]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1):                   
                        new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                        part2 = [new_macd_option_ema_slow]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1): 
                        if mem [0][1] == 0:
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option]
                            part3 = mem[0][i+1:]
                        if mem[0][1] == 2:
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option]
                            part3 = mem[0][i+1:]
                        if mem[0][1] == 3:
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option]
                            part3 = mem[0][i+1:]  
                    mem[0] = part1 + part2 + part3
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))

                if i == 5:
                    part1 = mem[0][:i]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1):                   
                        new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                        part2 = [new_macd_option_ema_fast]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1): 
                        if mem [0][1] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][i+1:]
                        if mem[0][1] == 2:
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][i+1:]
                        if mem[0][1] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][i+1:]
                    mem[0] = part1 + part2 + part3  
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))
                    
                if i == 6:
                    part1 = mem[0][:i]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1):                   
                        new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                        part2 = [new_macd_option_sma]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1): 
                        new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                        part2 = [new_macd_option_ema_slow]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1): 
                        if mem [0][2] == 0:
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option]
                            part3 = mem[0][i+1:]
                        if mem[0][2] == 2:
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option]
                            part3 = mem[0][i+1:]
                        if mem[0][2] == 3:
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option]
                            part3 = mem[0][i+1:]  
                    mem[0] = part1 + part2 + part3  
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))
                        
                if i == 7:
                    part1 = mem[0][:i]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1):                   
                        new_macd_value = 0
                        part2 = [new_macd_value]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1): 
                        new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                        part2 = [new_macd_option_ema_fast]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1): 
                        if mem [0][2] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][i+1:]
                        if mem[0][2] == 2:
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][i+1:]
                        if mem[0][2] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][i+1:]
                    mem[0] = part1 + part2 + part3  
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))

                if i == 8:
                    part1 = mem[0][:i]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1):                   
                        new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                        part2 = [new_macd_option_ema_slow]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1): 
                        new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                        part2 = [new_macd_option_sma]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1): 
                        if mem [0][2] == 0:
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option]
                            part3 = mem[0][i+1:]
                        if mem[0][2] == 2:
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option]
                            part3 = mem[0][i+1:]
                        if mem[0][2] == 3:
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option]
                            part3 = mem[0][i+1:]  
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1): 
                        if mem [0][3] == 0:
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 2:
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 3:
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option]
                            part3 = mem[0][i+1:] 
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1):
                        new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                        part2 = [new_macd_option_ema_slow]
                        part3 = mem[0][i+1:]                        
                    mem[0] = part1 + part2 + part3  
#                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))

                if i == 9:
                    part1 = mem[0][:i]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1):                   
                        new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                        part2 = [new_macd_option_ema_fast]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1): 
                        new_macd_value = 0
                        part2 = [new_macd_value]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1):                       
                        if mem[0][2] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][i+1:]     
                        if mem[0][2] == 2:                            
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][i+1:]
                        if mem[0][2] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][i+1:]                       
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1): 
                        if mem [0][3] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 2:
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][i+1:]  
                    mem[0] = part1 + part2 + part3 
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))
          
                if i == 10:
                    part1 = mem[0][:i]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1):                   
                        new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                        part2 = [new_macd_option_sma]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1): 
                        new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                        part2 = [new_macd_option_ema_slow]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1):                       
                        if mem [0][3] == 0:
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 2:
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 3:
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option]
                            part3 = mem[0][i+1:]              
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1): 
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]
                    mem[0] = part1 + part2 + part3 
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))

                if i == 11:
                    part1 = mem[0][:i]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1):                   
                        new_macd_value = 0
                        part2 = [new_macd_value]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1): 
                        new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                        part2 = [new_macd_option_ema_fast]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1):                       
                        if mem [0][3] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 2:
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][i+1:]      
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1): 
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]
                    mem[0] = part1 + part2 + part3 
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))

                if i == 12:
                    part1 = mem[0][:i]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1):                 
                        new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                        part2 = [new_macd_option_ema_slow]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1): 
                        new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                        part2 = [new_macd_option_sma]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1):                       
                        if mem [0][3] == 0:
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 2:
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 3:
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option]
                            part3 = mem[0][i+1:]        
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1): 
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]
                    mem[0] = part1 + part2 + part3 
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))

                if i == 13:
                    part1 = mem[0][:i]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1):                 
                        new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                        part2 = [new_macd_option_ema_fast]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1): 
                        new_macd_value = 0
                        part2 = [new_macd_value]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1):                       
                        if mem [0][3] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 2:
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][i+1:]        
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1): 
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1):
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]
                    mem[0] = part1 + part2 + part3 
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))

                if i == 14:
                    part1 = mem[0][:i]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1):                 
                        new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                        part2 = [new_macd_option_sma]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1): 
                        new_comp = list_comparators[random.randint(0,5)]
                        part2 = [new_comp]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1):
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]
                    mem[0] = part1 + part2 + part3 
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))

                if i == 15:
                    part1 = mem[0][:i]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1):                 
                        new_macd_value = 0
                        part2 = [new_macd_value]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1): 
                        new_comp = list_comparators[random.randint(0,5)]
                        part2 = [new_comp]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1):
                        new_logical = random.randint(0,1)
                        part2 = [new_logical]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1):
                        new_order = random.randint(0,1)
                        if new_order == mem[1][-1]:
                            if new_order == 1:
                                mem[1][-1] = 0
                            else:
                                mem[1][-1] = 1
                        part2 = [new_order]
                        part3 = mem[0][i+1:]                 
                    mem[0] = part1 + part2 + part3 
                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))


                if len(mem[0]) == 22:
                    if i == 16:
                        part1 = mem[0][:i]
                        if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1):                 
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]                    
                        if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1):
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]                  
                        mem[0] = part1 + part2 + part3 
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))
                    
                    if i == 17:
                        part1 = mem[0][:i]
                        if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1):                 
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]                    
                        if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1): 
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]  
                        if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1):
                            new_order = random.randint(0,1)
                            if new_order == mem[1][-1]:
                                if new_order == 1:
                                    mem[1][-1] = 0
                                else:
                                    mem[1][-1] = 1
                                part2 = [new_order]
                                part3 = mem[0][i+1:] 
                        mem[0] = part1 + part2 + part3 
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))

                    if i == 18:
                        part1 = mem[0][:i]
                        if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1):                 
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]                    
                        if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1): 
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]  
                        mem[0] = part1 + part2 + part3 
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))

                    if i == 19:
                        part1 = mem[0][:i]
                        if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1):                 
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]                    
                        if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1): 
                            new_order = random.randint(0,1)
                            if new_order == mem[1][-1]:
                                if new_order == 1:
                                    mem[1][-1] = 0
                                else:
                                    mem[1][-1] = 1
                                part2 = [new_order]
                                part3 = mem[0][i+1:] 
                        mem[0] = part1 + part2 + part3
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))

                    if i == 20:
                        part1 = mem[0][:i]
                        if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1):                 
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]                                       
                        mem[0] = part1 + part2 + part3
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))

                    if i == 21:
                        part1 = mem[0][:i]
                        if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1):                 
                            new_order = random.randint(0,1)
                            if new_order == mem[1][-1]:
                                if new_order == 1:
                                    mem[1][-1] = 0
                                else:
                                    mem[1][-1] = 1
                            part2 = [new_order]
                            part3 = mem[0][i+1:]                                        
                        mem[0] = part1 + part2 + part3
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))

                if len(mem[0]) == 20:
                    if i == 16:
                        part1 = mem[0][:i]
                        if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1):                 
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]                    
                        if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1):
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]                  
                        mem[0] = part1 + part2 + part3 
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))
                    
                    if i == 17:
                        part1 = mem[0][:i]
                        if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1):                 
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]                    
                        if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1): 
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]  
                        if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1):
                            new_order = random.randint(0,1)
                            if new_order == mem[1][-1]:
                                if new_order == 1:
                                    mem[1][-1] = 0
                                else:
                                    mem[1][-1] = 1
                                part2 = [new_order]
                                part3 = mem[0][i+1:] 
                        mem[0] = part1 + part2 + part3 
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))

                    if i == 18:
                        part1 = mem[0][:i]
                        if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1):                 
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]                    
                        if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1): 
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]  
                        mem[0] = part1 + part2 + part3 
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))

                    if i == 19:
                        part1 = mem[0][:i]
                        if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1):                 
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]                    
                        if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1): 
                            new_order = random.randint(0,1)
                            if new_order == mem[1][-1]:
                                if new_order == 1:
                                    mem[1][-1] = 0
                                else:
                                    mem[1][-1] = 1
                            part2 = [new_order]
                            part3 = mem[0][i+1:] 
                        mem[0] = part1 + part2 + part3
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))

                if len(mem[0]) == 18:
                    if i == 16:                        
                        part1 = mem[0][:i]
                        if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1):                 
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]                    
                        if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1):
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]                  
                        mem[0] = part1 + part2 + part3 
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))
                    
                    if i == 17:
                        part1 = mem[0][:i]
                        if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1):                 
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]                    
                        if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1): 
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]  
                        if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1):
                            new_order = random.randint(0,1)
                            if new_order == mem[1][-1]:
                                if new_order == 1:
                                    mem[1][-1] = 0
                                else:
                                    mem[1][-1] = 1
                            part2 = [new_order]
                            part3 = mem[0][i+1:] 
                        mem[0] = part1 + part2 + part3 
                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])))
                
    if mem[0][0] == 4:   
        i=0
        while(i<len(mem[0])):
            rand = round (random.uniform(0,1),2)
            if rand < 0.99:
                if i == 5:
                    part1 = mem[0][:i]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) :
                        if mem [0][1] == 0:
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option]
                            part3 = mem[0][i+1:]
                        if mem[0][1] == 2:
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option]
                            part3 = mem[0][i+1:]
                        if mem[0][1] == 3:
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option]
                            part3 = mem[0][i+1:]
                        
                    if (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) :
                        new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                        part2 = [new_macd_option_ema_slow]                                           
                        part3 = mem[0][i+1:]
#                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))

                    mem[0]= part1 + part2 + part3
                
                if i == 6:
                    part1 = mem[0][:i]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) :
                        if mem [0][1] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][i+1:]
                        if mem[0][1] == 2:
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][i+1:]
                        if mem[0][1] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][i+1:] 
                    if (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) :
                        new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                        part2 = [new_macd_option_ema_fast]                    
                        part3 = mem[0][i+1:]
                    mem[0]= part1 + part2 + part3
#                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    
                if i == 7:
                    part1 = mem[0][:i]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        if mem [0][2] == 0:
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option]
                            part3 = mem[0][i+1:]
                        if mem[0][2] == 2:
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option]
                            part3 = mem[0][i+1:]
                        if mem[0][2] == 3:
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option]
                            part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                        part2 = [new_macd_option_ema_slow]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) :
                        new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                        part2 = [new_macd_option_sma]
                        part3 = mem[0][i+1:]
                    mem[0]= part1 + part2 + part3
#                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    
                if i == 8:
                    part1 = mem[0][:i]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        if mem [0][2] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][i+1:]
                        if mem[0][2] == 2:
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][i+1:]
                        if mem[0][2] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                        part2 = [new_macd_option_ema_fast]                    
                        part3 = mem[0][i+1:]
                    if (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) :
                        new_macd_value = 0
                        part2 = [new_macd_value]                    
                        part3 = mem[0][i+1:]
                    mem[0]= part1 + part2 + part3
#                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                
                if i == 9:
                    part1 = mem[0][:i]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ):
                        if mem [0][3] == 0:
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 2:
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 3:
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option]
                            part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                        part2 = [new_macd_option_sma]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        if mem [0][2] == 0:
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option]
                            part3 = mem[0][i+1:]
                        if mem[0][2] == 2:
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option]
                            part3 = mem[0][i+1:]
                        if mem[0][2] == 3:
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option]
                            part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                        part2 = [new_macd_option_ema_slow]
                        part3 = mem[0][i+1:]
                    mem[0]= part1 + part2 + part3
#                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    
                if i == 10:
                    part1 = mem[0][:i]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ):
                        if mem [0][3] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 2:
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                        part2 = [new_macd_option_ema_fast]                    
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_value = 0
                        part2 = [new_macd_value]                    
                        part3 = mem[0][i+1:]
                    if (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        if mem [0][2] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][i+1:]
                        if mem[0][2] == 2:
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][i+1:]
                        if mem[0][2] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][i+1:]    
                    mem[0]= part1 + part2 + part3
#                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    
                if i == 11:
                    part1 = mem[0][:i]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ):
                        if mem [0][4] == 0:
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option]
                            part3 = mem[0][i+1:]
                        if mem[0][4] == 2:
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option]
                            part3 = mem[0][i+1:]
                        if mem[0][4] == 3:
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option]
                            part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                        part2 = [new_macd_option_ema_slow]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                        part2 = [new_macd_option_sma]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ):
                        if mem [0][3] == 0:
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 2:
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 3:
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option]
                            part3 = mem[0][i+1:]
                    mem[0]= part1 + part2 + part3
#                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    
                if i == 12:
                    part1 = mem[0][:i]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ):
                        if mem [0][4] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][i+1:]
                        if mem[0][4] == 2:
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][i+1:]
                        if mem[0][4] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                        part2 = [new_macd_option_ema_fast]                    
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_value = 0
                        part2 = [new_macd_value]                    
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ):
                        if mem [0][3] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 2:
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][i+1:] 
                    mem[0]= part1 + part2 + part3
#                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    
                if i == 13:
                    part1 = mem[0][:i]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ):
                        new_comp = list_comparators[random.randint(0,5)]
                        part2 = [new_comp]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                        part2 = [new_macd_option_sma]
                        part3 = mem[0][i+1:]
                    if(mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ):
                        if mem [0][4] == 0:
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option]
                            part3 = mem[0][i+1:]
                        if mem[0][4] == 2:
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option]
                            part3 = mem[0][i+1:]
                        if mem[0][4] == 3:
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option]
                            part3 = mem[0][i+1:]
                    if(mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                        part2 = [new_macd_option_ema_slow]
                        part3 = mem[0][i+1:]
                    if(mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ):
                        if mem [0][3] == 0:
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 2:
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 3:
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option]
                            part3 = mem[0][i+1:]               
                    mem[0]= part1 + part2 + part3
#                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    
                if i == 14:
                    part1 = mem[0][:i]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ):
                        new_comp = list_comparators[random.randint(0,5)]
                        part2 = [new_comp]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ):
                        new_macd_value = 0
                        part2 = [new_macd_value]                    
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ):
                        if mem [0][4] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][i+1:]
                        if mem[0][4] == 2:
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][i+1:]
                        if mem[0][4] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                            new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                            part2 = [new_macd_option_ema_fast]                    
                            part3 = mem[0][i+1:]
                    if(mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 )or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                       new_macd_value = 0
                       part2 = [new_macd_value]                    
                       part3 = mem[0][i+1:]   
                    if(mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ): 
                        if mem [0][3] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 2:
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][i+1:]
                        if mem[0][3] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][i+1:]                
                    mem[0]= part1 + part2 + part3
#                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    
                if i == 15:
                    part1 = mem[0][:i]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 )or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ):
                        new_comp = list_comparators[random.randint(0,5)]
                        part2 = [new_comp]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 )or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                        part2 = [new_macd_option_sma]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ):
                        if mem [0][4] == 0:
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option]
                            part3 = mem[0][i+1:]
                        if mem[0][4] == 2:
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option]
                            part3 = mem[0][i+1:]
                        if mem[0][4] == 3:
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option]
                            part3 = mem[0][i+1:]            
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ):
                        new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                        part2 = [new_macd_option_ema_slow]
                        part3 = mem[0][i+1:]
                    mem[0]= part1 + part2 + part3
#                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    
                if i == 16:
                    part1 = mem[0][:i]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 )or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ):
                        new_comp = list_comparators[random.randint(0,5)]
                        part2 = [new_comp]
                        part3 = mem[0][i+1:]     
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 )or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_value = 0
                        part2 = [new_macd_value]                    
                        part3 = mem[0][i+1:]       
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ):
                        if mem [0][4] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][i+1:]
                        if mem[0][4] == 2:
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][i+1:]
                        if mem[0][4] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ):
                        new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                        part2 = [new_macd_option_ema_fast]                    
                        part3 = mem[0][i+1:]
                    mem[0]= part1 + part2 + part3
#                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
        
                if i == 17:
                    part1 = mem[0][:i]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ):
                        new_logical = random.randint(0,1)
                        part2 = [new_logical]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 )or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 )   or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ):
                        new_comp = list_comparators[random.randint(0,5)]
                        part2 = [new_comp]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 )or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ):
                        new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                        part2 = [new_macd_option_sma]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ):
                        if mem [0][4] == 0:
                            new_sma_option = SMA_range_options[random.randint(0,6)]
                            part2 = [new_sma_option]
                            part3 = mem[0][i+1:]
                        if mem[0][4] == 2:
                            new_rsi_option = RSI_range_options[random.randint(0,4)]
                            part2 = [new_rsi_option]
                            part3 = mem[0][i+1:]
                        if mem[0][4] == 3:
                            new_mom_option = Momentum_range_options
                            part2 = [new_mom_option]
                            part3 = mem[0][i+1:]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_option_ema_slow = MACD_range_options_EMA_slow[random.randint(0,1)]
                        part2 = [new_macd_option_ema_slow]
                        part3 = mem[0][i+1:]
                    mem[0]= part1 + part2 + part3
#                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    
                if i == 18:
                    part1 = mem[0][:i]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ):
                        new_logical = random.randint(0,1)
                        part2 = [new_logical]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 )or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 )   or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ):
                        new_comp = list_comparators[random.randint(0,5)]
                        part2 = [new_comp]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 )or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ):
                        new_macd_value = 0
                        part2 = [new_macd_value]                    
                        part3 = mem[0][i+1:] 
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ):
                        if mem [0][4] == 0:
                            new_sma_value = SMA_range_values[random.randint(0,10)]
                            part2 = [new_sma_value]
                            part3 = mem[0][i+1:]
                        if mem[0][4] == 2:
                            new_rsi_value = RSI_range_values
                            part2 = [new_rsi_value]
                            part3 = mem[0][i+1:]
                        if mem[0][4] == 3:
                            new_mom_value = Momentum_range_values
                            part2 = [new_mom_value]
                            part3 = mem[0][i+1:]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_option_ema_fast = MACD_range_options_EMA_fast[random.randint(0,1)]
                        part2 = [new_macd_option_ema_fast]                    
                        part3 = mem[0][i+1:]
                    mem[0]= part1 + part2 + part3
#                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    
                if i == 19:
                    part1 = mem[0][:i]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 )or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ):
                        new_logical = random.randint(0,1)
                        part2 = [new_logical]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 )   or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or(mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 )or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ):
                        new_comp = list_comparators[random.randint(0,5)]
                        part2 = [new_comp]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_option_sma = MACD_range_options_SMA[random.randint(0,1)]
                        part2 = [new_macd_option_sma]
                        part3 = mem[0][i+1:]
                    mem[0]= part1 + part2 + part3
#                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
        
                        
                if i == 20:
                    part1 = mem[0][:i]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ):
                        new_order = random.randint(0,1)
                        if new_order == mem[1][-1]:
                            if new_order == 1:
                                mem[1][-1] = 0
                            else:
                                mem[1][-1] = 1
                        part2 = [new_order]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 )or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ):
                        new_logical = random.randint(0,1)
                        part2 = [new_logical]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 )   or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or(mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 )or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ):
                        new_comp = list_comparators[random.randint(0,5)]
                        part2 = [new_comp]
                        part3 = mem[0][i+1:]
                    if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                        new_macd_value = 0
                        part2 = [new_macd_value]                    
                        part3 = mem[0][i+1:]
                    mem[0]= part1 + part2 + part3
#                    print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                    
                if len(mem[0]) == 29:
                    if i == 21:
                        part1 = mem[0][:i]
                        if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 )or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 )   or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ):                                 
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]                 
                        if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or(mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 )or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]
                        mem[0]= part1 + part2 + part3
#                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                        
                    if i==22:
                        part1 = mem[0][:i]
                        if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 )or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ):
                            new_order = random.randint(0,1)
                            if new_order == mem[1][-1]:
                                if new_order == 1:
                                    mem[1][-1] = 0
                                else:
                                    mem[1][-1] = 1
                            part2 = [new_order]
                            part3 = mem[0][i+1:]
                        if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 )   or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ):
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]
                        if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or(mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 )or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]
                        mem[0]= part1 + part2 + part3
#                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                        
                    if i ==23:
                        part1 = mem[0][:i]
                        if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 )   or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or(mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 )or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ):
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]
                        if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]
                        mem[0]= part1 + part2 + part3   
#                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                        
                    if i ==24:
                        part1 = mem[0][:i]
                        if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 )   or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ):
                            new_order = random.randint(0,1)
                            if new_order == mem[1][-1]:
                                if new_order == 1:
                                    mem[1][-1] = 0
                                else:
                                    mem[1][-1] = 1
                            part2 = [new_order]
                            part3 = mem[0][i+1:] 
                        if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or(mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 )or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ):
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]
                        if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]
                        mem[0]= part1 + part2 + part3  
#                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                        
                    if i ==25:
                        part1 = mem[0][:i]
                        if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or(mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 )or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]
                        mem[0]= part1 + part2 + part3  
#                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                        
                    if i ==26:
                        part1 = mem[0][:i]
                        if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or(mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 )or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) :
                            new_order = random.randint(0,1)
                            if new_order == mem[1][-1]:
                                if new_order == 1:
                                    mem[1][-1] = 0
                                else:
                                    mem[1][-1] = 1
                            part2 = [new_order]
                            part3 = mem[0][i+1:]         
                        if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]
                        mem[0]= part1 + part2 + part3  
#                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
        
                            
                    if i ==27:
                        part1 = mem[0][:i]
                        if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]
                        mem[0]= part1 + part2 + part3
#                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                        
                    if i ==28:
                        part1 = mem[0][:i]
                        if (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                            new_order = random.randint(0,1)
                            if new_order == mem[1][-1]:
                                if new_order == 1:
                                    mem[1][-1] = 0
                                else:
                                    mem[1][-1] = 1
                            part2 = [new_order]
                            part3 = mem[0][i+1:]   
                        mem[0]= part1 + part2 + part3
#                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                        
                if len(mem[0]) == 23:
                    if i == 21:
                        part1 = mem[0][:i]
                        if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 )or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 )   or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ):                                 
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]                 
                        if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or(mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 )or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]
                        mem[0]= part1 + part2 + part3
#                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
                        
                    if i==22:
                        part1 = mem[0][:i]
                        if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 )or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] != 1 ):
                            new_order = random.randint(0,1)
                            if new_order == mem[1][-1]:
                                if new_order == 1:
                                    mem[1][-1] = 0
                                else:
                                    mem[1][-1] = 1
                            part2 = [new_order]
                            part3 = mem[0][i+1:]
                        if (mem[0][1] != 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 )   or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] != 1 and mem[0][4] == 1 ):
                            new_logical = random.randint(0,1)
                            part2 = [new_logical]
                            part3 = mem[0][i+1:]
                        if (mem[0][1] != 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ) or(mem[0][1] == 1 and mem[0][2] != 1 and mem[0][3] == 1 and mem[0][4] == 1 )or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] != 1 and mem[0][4] == 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] != 1 ) or (mem[0][1] == 1 and mem[0][2] == 1 and mem[0][3] == 1 and mem[0][4] == 1 ):
                            new_comp = list_comparators[random.randint(0,5)]
                            part2 = [new_comp]
                            part3 = mem[0][i+1:]
                        mem[0]= part1 + part2 + part3
#                        print('i = ' + str(i) + ', length of mem[0] is :' + str(len(mem[0])) + ' length of part2 = ' + str(len(part2)) + ' length of part1 = ' + str(len(part1)))
          
            
                            
            i = i + 1
          
    return mem

def crossover(rule1_pool, rule2_pool, number_indicators):
    new_rule = []
    i = 0
    if number_indicators ==2:
        if(len(rule1_pool) == 11):# NO MACD
            midpoint = random.randint(7,9)           
            while(i<10):
                if(i<midpoint):
                    new_rule.append(rule1_pool)
                    i = i+ 1
                else:
                    new_rule.append(rule2_pool)
                    i = i+ 1
        if(len(rule1_pool) == 13): # 1 MACD
            midpoint = random.randint(9,11)
            while(i<12):
                if(i<midpoint):
                    new_rule.append(rule1_pool)
                    i = i+ 1
                else:
                    new_rule.append(rule2_pool)
                    i = i+ 1
        if(len(rule1_pool) == 15): # 2 MACD
            midpoint = random.randint(11,13)
            while(i<14):
                if(i<midpoint):
                    new_rule.append(rule1_pool)
                    i = i+ 1
                else:
                    new_rule.append(rule2_pool)
                    i = i+ 1
    if number_indicators == 3:################
        if(len(rule1_pool) == 16):# NO MACD
            midpoint= random.randint(10,14)
            while(i<15):
                if (i<midpoint):
                    new_rule.append(rule1_pool)
                    i = i + 1
                else:
                    new_rule.append(rule2_pool)
                    i = i+ 1
        if(len(rule1_pool) == 18): # 1 MACD
            midpoint = random.randint(12,16)
            while(i<17):
                if(i<midpoint):
                    new_rule.append(rule1_pool)
                    i = i+1
                else:
                    new_rule.append(rule2_pool)
                    i = i + 1
        if(len(rule1_pool) == 20): # 2 MACD
            midpoint = random.randint(14,18)
            while(i<19):
                if(i<midpoint):
                    new_rule.append(rule1_pool)
                    i = i+1
                else:
                    new_rule.append(rule2_pool)
                    i = i + 1
        if(len(rule1_pool) == 22): # 3 MACD
            midpoint = random.randint(16,20)
            while(i<21):
                if(i<midpoint):
                    new_rule.append(rule1_pool)
                    i = i+1
                else:
                    new_rule.append(rule2_pool)
                    i = i+ 1
    if number_indicators == 4:################
        if(len(rule1_pool) == 21):# NO MACD
            midpoint= random.randint(13,19)
            while(i<20):
                if (i<midpoint):
                    new_rule.append(rule1_pool)
                    i = i + 1
                else:
                    new_rule.append(rule2_pool)
                    i = i+ 1
        if(len(rule1_pool) == 23):# 1 MACD
            midpoint= random.randint(15,21)
            while(i<22):
                if (i<midpoint):
                    new_rule.append(rule1_pool)
                    i = i + 1
                else:
                    new_rule.append(rule2_pool)
                    i = i+ 1
        if(len(rule1_pool) == 25):# 2 MACD
            midpoint= random.randint(17,23)
            while(i<24):
                if (i<midpoint):
                    new_rule.append(rule1_pool)
                    i = i + 1
                else:
                    new_rule.append(rule2_pool)
                    i = i+ 1
        if(len(rule1_pool) == 27):# 3 MACD
            midpoint= random.randint(19,25)
            while(i<26):
                if (i<midpoint):
                    new_rule.append(rule1_pool)
                    i = i + 1
                else:
                    new_rule.append(rule2_pool)
                    i = i+ 1
        if(len(rule1_pool) == 29):# 4 MACD
            midpoint= random.randint(21,27)
            while(i<28):
                if (i<midpoint):
                    new_rule.append(rule1_pool)
                    i = i + 1
                else:
                    new_rule.append(rule2_pool)
                    i = i+ 1
                    
    return new_rule
    
def run():
    #generate population of random members
#1 member = 2 rules
#append the rules to the backtesting part
#backtest each member on the same period and same currency
#score each member based on the backtesting
#while some condition:
    #create a mating pool : repeat each member the number of times its score
    #do crossover and mutation on the pool
    #score each member
    i = 0
    population = []
    while(i<5):
        population.append(create_member())
        i = i + 1
    for element in population:
        write_in_python_file(element[0],element[0][0])
   
#run()
#test = []
#test.append(create_member())
##test.append(create_member())
#for e in test:
#    print(e)
#print(create_member())


def print_beginning_file():
    beg_file = []       
    test = open('backtrader_test.py','r')
    #beginning_file = test.readline()
    i = 0
    while (i<23):
        beg_file.append(test.readline())
        i = i+1
    #print(beginning_file)
    test.close()   
    test2 = open('rule_writing.txt','w')
    test2.writelines(''.join(beg_file))  
    test2.close()
#print_beginning_file()
#end_file = []    
def print_end_file():   
    test = open('end_file_backtrader.py','r')
    end_file = test.readlines()
#    print(end_file)
    
    #print(beginning_file)
    test.close()   
    test2 = open('backtesting_file_end.py','w')
    test2.writelines(''.join(end_file))  
    test2.close()
#print_end_file()
print_beginning_file()
test = create_member()
#array = [[2, 1, 2, 30, 15, 5, 0, 50, 86, 3, 4, 0, 0], [2, 0, 3, 90, 'SMA(10)', 11, 108.47, 5, 2, 1, 1]]
print(test)
#print(options_listm)
#print(test)
#write_in_python_file(test[0],test[0][0])
#print(str(count))
#write_in_python_file(test[1],test[1][0])
  
                
    
             
                    
#test = create_member()
#print(test)
#print(test)
#print(len(test))                  
#array = [[2,3,1,11,96.18,15,20,25,0,2,2,1,1],[2,1,1,15,20,25,0,15,30,5,0,0,0,1,0]]                        
#test = create_member()
#print(array)
#print(create_member())

array = [1,2,3,4,5,6,7,8]
# i = 4 ( value = 5)
i = 4
#print('print from beginning to element before 5 : ' + str(array[:i]))
#
#print('print from 6 to end : ' +str(array[i+1:]))


#
#print('rule before mutation : ' + str(test[0]))
#print(len(test[0]))
#new = mutate(test)
#print('rule after mutation : ' + str(new[0]))  
##print(len(new[0]))
#print(create_rule())





#print(str(round(random.uniform(0,1),2)))                  
    
#    i = 0
#    member_array = []
#    print(mem)
#    test = mem[0] + mem[1]
    
#    return test
        
#(mutate(create_member()))
#test = cre

            
            
    
    
        
        
        
        
        
        
        
