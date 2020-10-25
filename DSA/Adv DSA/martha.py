# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 21:18:31 2020

@author: KayDee
"""
from itertools import permutations
T = int(input())
while T:
    cmd = input()
    x1,y1 = list(map(int,input().split()))
    Q = int(input())
    mainl = {"U":0,"D":0,"R":0,"L":0}
    for j in cmd:
       
                
        mainl[j] += 1
    
    for _ in range(Q):
        maint = mainl.copy()
        R,L,D,U =0,0,0,0
        x2,y2 = list(map(int,input().split()))
        if x1 > x2:
            L=abs(x1-x2)
        elif x2 > x1:
            R=abs(x2-x1)
        if y1 > y2:
            D=abs(y1-y2)
        elif y1 < y2:
            U =abs(y2-y1)
            
        maint["R"] -= R
        maint["U"] -= U
        maint["L"] -= L
        maint["D"] -= D
            
        
        res2 = R+L+D+U
        for x in maint:
            if maint[x]<0:
                print("NO")
                break
        else:
            print("YES",res2)
    
        
    
    
    #print(s)
            
            
    T-=1