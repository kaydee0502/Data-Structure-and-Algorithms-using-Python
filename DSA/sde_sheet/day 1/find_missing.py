#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 12:22:54 2021

@author: kaydee
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        act = (n*(n+1))//2
        giv = sum(nums)
        return act-giv