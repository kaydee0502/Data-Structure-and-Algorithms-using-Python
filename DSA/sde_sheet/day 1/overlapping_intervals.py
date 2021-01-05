#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 13:25:53 2021

@author: kaydee
"""

class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        
        intervals.sort()
        
        start = intervals[0][0]
        stop = intervals[0][1]
        
        res = []
        
        for i in range(1,len(intervals)):
            if intervals[i][0] > stop:
                res.append([start,stop])
                start = intervals[i][0]
                stop = intervals[i][1]
                
            elif intervals[i][1] > stop:
                stop = intervals[i][1]
        
        res.append([start,stop])
        
        return res
                
        