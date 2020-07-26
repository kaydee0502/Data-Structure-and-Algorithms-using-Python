# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:49:51 2020

@author: KayDee
"""
import time
import matplotlib.pyplot as plt
import numpy as np

Nemo = [x for x in range(10)]
print(Nemo)

def function(list):
    x = []
    y = []
    w = 0
    tt = 0
    function.t0 = time.time()
    for a in range(len(list)):
        function.t2 = time.time()
        for b in range(len(list)):
            print(list[a],list[b])
            x.append(w)
            w += 1
            function.t3 = time.time()
            tt += function.t3-function.t2
            y.append(tt)
    function.t1 = time.time()
    
        
function(Nemo)
print('Time taken : {}'.format(function.t1-function.t0) + ' seconds')

d = dict([['name','kd']])