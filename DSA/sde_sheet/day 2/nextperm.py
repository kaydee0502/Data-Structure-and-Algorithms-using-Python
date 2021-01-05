#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 16:10:06 2021

@author: kaydee
"""

class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] < nums[i]:
                for nb in range(i,len(nums)):
                    if nums[nb] <= nums[i-1]:
                        print(i,nb)
                        nb = nb-1
                        break
                nums[i-1],nums[nb] = nums[nb],nums[i-1]
                l = len(nums[i:])//2
                left = i
                right = len(nums)-1
                
                while l:
                    nums[left],nums[right] = nums[right],nums[left]
                    left+=1
                    right-=1
                    l-=1
                
                break
        else:
            nums.sort()
                    
        print(nums)
            
        