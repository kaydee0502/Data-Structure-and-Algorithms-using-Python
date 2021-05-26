#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        s = []
        r = {}
        for i in s:
            if i in ['(', '{', '[']:
                s.append(i)
            if i in [')', '}', ']']:
                f = s.pop()
                if i == ')' and f != '(':
                    return False
                if i == '}' and f != '{':
                    return False
                if i == ']' and f != '[':
                    return False
        if len(s) == 0:
            return True
        
# @lc code=end

