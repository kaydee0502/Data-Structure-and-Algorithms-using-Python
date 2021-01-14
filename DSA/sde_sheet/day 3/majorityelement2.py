#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:06:59 2021

@author: kaydee
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj1 = float("inf")
        maj2 = float("inf")
        
        c1 = 0
        c2 = 0
        
        
        for i in range(len(nums)):
            if nums[i] == maj1:
                c1+=1
                
            elif nums[i] == maj2:
                c2+=1
                
            elif c1 == 0:
                c1+=1
                maj1 = nums[i]
                
            elif c2 == 0:
                c2+=1
                maj2 = nums[i]
                
            else:
                c1-=1
                c2-=1
               
        res = [] 
        
        c1 = 0
        c2 = 0
        
        for i in nums:
            if i == maj1:
                c1+=1
            elif i == maj2:
                c2+=1
        print(c1,c2)
        if c1 > len(nums)/3:
            res.append(maj1)
            
        if c2 > len(nums)/3:
            res.append(maj2)
            
        return res