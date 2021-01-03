#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:02:14 2021

@author: kaydee
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        maxlen = len(nums1)
        if m == 0:
            for i in range(maxlen):
                nums1[i] = nums2[i]
        i = m-1
        j = n-1
        k = maxlen-1
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k-=1
                i-=1
            else:
                nums1[k] = nums2[j]
                k-=1
                j-=1
                
        while i >= 0:
            nums1[k] = nums1[i]
            k-=1
            i-=1
            
        while j >= 0:
            nums1[k] = nums2[j]
            k-=1
            j-=1
            
    
        
        
        
        