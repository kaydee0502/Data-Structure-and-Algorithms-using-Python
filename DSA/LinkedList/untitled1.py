#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 12:41:05 2021

@author: kaydee
"""

from aditi_LL import Linklist


def f(head):
    if not head:
        return 
    if not head.next:
        return
    
    f(head.next.next)
    print(head.data)


ml = Linklist()

for i in range(1,10):
    ml.append(i)
    
f(ml.head)