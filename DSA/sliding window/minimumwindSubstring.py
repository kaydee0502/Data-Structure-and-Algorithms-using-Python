'''

76. Minimum Window Substring
Hard

6434

436

Add to List

Share
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"
 

Constraints:

1 <= s.length, t.length <= 10^5
s and t consist of English letters.
 

Follow up: Could you find an algorithm that runs in O(n) time?

'''

from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        H = {}
        
        i = 0
        j = 0
        mlen = float("inf")
        slide = deque()
        check = {}
        inds = []
        if len(t) > len(s):
            return ""
        
        if len(t) == 1:
            if t in s:
                return t
            else:
                return ""
             
        for k in t:
            if not k in H:
                H[k] = 0
            H[k]+=1
                
       

        while j < len(s):
            #print(H)
            #print(j,mlen,slide)
            if s[j] in H:
          
                H[s[j]] -= 1
                slide.append([s[j],j])
                  
                    
                    
                if slide[0][0] == s[j] and H[s[j]] <= 0:

                    while 1:
                      
                        #slide.append([s[j],j])
                        if H[slide[0][0]] >= 0:
                            break
                        else:
                            H[slide[0][0]] += 1
                            
                        slide.popleft()

                        #if check[slide[0][0]] <= 1:
                        #    break

               
                #print(H.values(),list(filter(lambda x: x>0,H.values())),slide)
                if not list(filter(lambda x: x>0,H.values())):
                        print(H.values())
                        if slide[-1][1] - slide[0][1] + 1 < mlen:
                            inds = [slide[0][1],slide[-1][1]]
                            mlen = slide[-1][1] - slide[0][1] + 1
                            
                                

                          
                        
                        
                        
            j+=1
            
        
            
        print(mlen,slide)
        #if len(check) != len(t):
        #    return ""
        print(inds)
        if inds:
            
            desired = s[inds[0]:inds[1]+1] 
            return desired
        return ""                
                            
                            
                            
                        
                    
                    
                    
                    
                
                    
            
            
            
        
