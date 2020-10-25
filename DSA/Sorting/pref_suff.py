.# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 16:29:00 2020

@author: KayDee
"""

string = input("Input : ")
a = string[:len(string)//2]
b = string[len(string)//2:]
count = []
for i in range(len(a)+1):
    
    
    c = b[-1:-(len(a[:i])+1):-1]
    if a[:i] == c[::-1]:
        count.append(len(a[:i]))
        
        #print(a[:i])
    
print(max(count))