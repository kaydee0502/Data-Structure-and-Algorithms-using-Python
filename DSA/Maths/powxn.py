'''
50. Pow(x, n)
Medium

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        isNeg = False
        
        if n < 0:
            isNeg = True
        if n == 0:
            return 1.0
        print(isNeg)
        n = abs(n)
        ans = x
        ext = 1
        while n > 1:
            if n%2 != 0:
                ext*= ans
                n-=1
            else:
                ans = ans*ans
                n = n//2
                
        if isNeg:
            return 1/(ans*ext)
        return ans*ext
