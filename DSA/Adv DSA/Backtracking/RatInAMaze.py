# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 21:30:56 2020

@author: KayDee
"""

path = ""

def printSol(s):
    global path
    print(*s,sep="\n")
    print(path)
    print()
    path = path[:-1]
    #path = ""
    
    return

def helper(maze,solution,n,x,y,way):
    global path
    
    if x == n-1 and y == n-1:
        solution[x][y] = 1
        path += way
        
        
        printSol(solution)
        print()
        return
        
    if x < 0 or y < 0 or x > n-1 or y > n-1 or maze[x][y] == 0 or solution[x][y] == 1:
        return
    
    solution[x][y] = 1
    path += way
    helper(maze,solution,n,x+1,y,"D")
    helper(maze,solution,n,x-1,y,"U")
    helper(maze,solution,n,x,y+1,"R")
    helper(maze,solution,n,x,y-1,"L")
    
    solution[x][y] = 0
    
    path = path[:-1]
    #print("deb",path)
    
    




def solve(maze,n):
    solution = [[0]*n for i in range(n)]
    #print(*solution,sep="\n")
    helper(maze,solution,n,0,0,"")
    




def main():
    n = int(input())
    a = []
    for i in range(n):
        l = list(map(int,input().split()))
        a.append(l)
        
    solve(a,n)
    
main()