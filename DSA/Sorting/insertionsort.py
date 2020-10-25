# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 17:25:41 2020

@author: KayDee
"""

a = [2, 65, 32, 2, 1, 7, 8,1,1,1,0,-1]

def insertionsort(n):
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            temp = n[i+1]
            print(temp)
            for j in range(i,-1,-1):
                
                n[j+1] = n[j]
               
                if n[j] < temp:
                    n[j+1] = temp
                    
                    print(n)
                    break
            else:
                n[j] = temp
                
    #print(n)
    return n
                
res = insertionsort(a) 
print(res)               
        
    