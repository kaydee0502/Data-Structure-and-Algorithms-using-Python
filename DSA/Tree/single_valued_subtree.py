#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 10:37:34 2021

@author: kaydee
"""

'''
Given a binary tree, count the number of Single Valued Subtrees. A Single Valued Subtree is one in which all the nodes have same value. 

Example 1

Input :
              5
             / \
            1   5
           / \   \
          5   5   5
Output : 4
Explanation : 
There are 4 subtrees with single values.

Example 2:

Input:
              5
             / \
            4   5
           / \   \
          4   4   5   
Output: 5
Explanation: 
There are five subtrees with single values.

Your task :
You don't have to read input or print anything. Your task is to complete the function singlevalued() which takes the root of the tree as input and returns the count of single valued subtrees.
 
Expected Time Complexity : O(n)
Expected Auxiliary Space : O(n)
 
Constraints :
1 <= n <= 10^5
'''


#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def singlevalued(self, root):
        
        sval = 0 #counter to keep track of singled valued subtrees
        
        def post(root):
            '''
            Post-order traversal of a binary tree
            
            
            Parameters
            ----------
            root : root node of tree
            
            Return
            ---------
            True if subtree is a single value tree, else false.
                
            '''
            
            
            nonlocal sval #use nonlocal variable sval
            
            
            # use a for left subtree
            a = None
            # use b for right subtree
            b = None
            
            
            #check left and right subtrees
            if root.left:
                a = post(root.left)
                
            if root.right:
                b = post(root.right)
                
                
            # Check if both subtree returned true and their value
            # matches with current root value, if it does, we found
            # a single valued subtree.
            
            # Condition 1: if both left and right are present    
            if a and b:
                
                if a[0] and b[0] and root.data == a[1] and root.data == b[1]:
                    print(root.data)
                    sval+=1
                else:
                    # Else return false
                    return [False,root.data]
                
            # Condition 2: if only left subtree is present    
            if a:
                
                if a[0] and a[1] == root.data:
                    sval+=1
                else:
                    return [False,root.data]
            # Condition 3: if only right subtree is present      
            if b:
                if b[0] and b[1] == root.data:
                    sval+=1
                else:
                    return [False,root.data]
                    
            
            # If current node is leaf tree, it is considered to be a
            # singled value tree
            if not root.left and not root.right:
                sval+=1
                return [True, root.data]
                
            
            
            
                
        post(root) # perform traversal
        return sval
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob= Solution()
        
        ans = ob.singlevalued(root)
        print(ans)
        

# } Driver Code Ends