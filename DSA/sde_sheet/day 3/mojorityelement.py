#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:41:02 2021

@author: kaydee
"""

class Solution:
    def majorityElement(self, nums) -> int:
        maj = nums[0]
        count = 1
        
        
        for i in range(1,len(nums)):
            
            if nums[i] == maj:
                count+=1
                
            else:
                print(maj,count)
                count-=1
                if count == 0:
                    maj = nums[i]
                    count = 1
                    
        return maj
            