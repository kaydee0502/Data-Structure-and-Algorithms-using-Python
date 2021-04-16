'''


131. Palindrome Partitioning
Medium

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]

 

Constraints:

    1 <= s.length <= 16
    s contains only lowercase English letters.




'''

class Solution:
    
    def isPalin(self,x):
        return x == x[::-1]
    
    
    def rec(self,s,p,r):
        
        
        if len(s) == 0:
            p.append(r)
        
        
        for i in range(len(s)):
            if self.isPalin(s[:i+1]):
                self.rec(s[i+1:],p,r+[s[:i+1]])
            
    
    
    def partition(self, s: str) -> List[List[str]]:
        
        part = []
        
        self.rec(s,part,[])
        
        return part
        
