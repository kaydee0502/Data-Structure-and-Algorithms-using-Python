#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:39:51 2021

@author: kaydee
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy = float("inf")
        sell = 0
        
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                
            elif prices[i]-buy > sell:
                sell = prices[i]-buy
                
        return sell