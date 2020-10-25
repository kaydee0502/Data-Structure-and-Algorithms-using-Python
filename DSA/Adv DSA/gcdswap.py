# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:28:22 2020

@author: KayDee
"""

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b)
    
t=int(input())
while t:
    n = int(input())
    arr = arr = list(map(int,input().split()))
    for i in range(1,n+1):
        if gcd(i,arr[i-1]) != arr[i-1]:
            print("NO")
            break
    else:
        print("YES")
    t-=1
    