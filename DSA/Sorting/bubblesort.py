# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 14:09:00 2020

@author: KayDee
"""

a = [2, 65, 32, 2, 1, 7, 8]

def bubblesort(n):
    
     while True: 
        swap = False
        for i in range(len(n)-1):
            if n[i] > n[i+1]:
              
                n[i],n[i+1] = n[i+1],n[i]
                swap = True
              
        if not swap:
            break
            
     return n
 

            

res = bubblesort(a)

print(res)

        