#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 12:10:53 2021

@author: kaydee
"""

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        s = 0
        r = len(nums)-1
        
        while 1:
            
            if nums[s] == 0:
                nums[l],nums[s] = nums[s],nums[l]
                l+=1
                s+=1
            elif nums[s] == 1:
                s+=1
            else:
                nums[r],nums[s] = nums[s],nums[r]
                r-=1
            print(nums,l,s,r)
            if l == r or s > r:
                break
            
        return nums