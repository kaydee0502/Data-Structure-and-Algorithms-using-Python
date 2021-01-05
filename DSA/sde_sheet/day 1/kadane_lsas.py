#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 12:42:49 2021

@author: kaydee
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lmax = float("-inf")
        gmax = lmax
        for i in range(len(nums)):
            lmax = max(nums[i],lmax+nums[i])
            if lmax > gmax:
                gmax = lmax
                
        return gmax