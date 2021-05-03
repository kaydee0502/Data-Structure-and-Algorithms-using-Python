'''

474. Ones and Zeroes
Medium

1872

291

Add to List

Share
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100

'''




class Solution:
    
    def f(self,st):
        o = 0
        z = 0
        for i in st:
            if i =="0":
                z+=1
            else:
                o+=1
                
        return o,z
    
    def r(self,s,m,n,strs):
        if s == 0 or (m == 0 and n == 0):
            return 0
        
        o,z = self.f(strs[s-1])
        #print(o,z,strs[s-1])
        
        if z <= m and o <= n:
            
            return max(1+self.r(s-1,m-z,n-o,strs),self.r(s-1,m,n,strs))
        else:
            return self.r(s-1,m,n,strs)
        
    
    
    
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self.r(len(strs),m,n,strs)