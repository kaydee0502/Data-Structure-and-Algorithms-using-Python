'''

424. Longest Repeating Character Replacement
Medium

2309

115

Add to List

Share
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:

1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length

'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        h = {}
        
        
        i = 0
        j = 0
        mfreq = 0
        mlen = 0
        
        while i < len(s):
            #print(i,j)
            
            if not s[i] in h:
                h[s[i]] = 0
                
            h[s[i]] +=1
            
            if  h[s[i]] > mfreq:
                mfreq = h[s[i]]
                
            if (i-j+1) - mfreq > k:
                
                h[s[j]] -= 1
                if h[s[j]] == 0:
                    h.pop(s[j])
                    
                
                
                j+=1
                
            else:
                mlen = max(mlen,i-j+1)
                
            i+=1
                
                
        return mlen
                
                
            
            
            
