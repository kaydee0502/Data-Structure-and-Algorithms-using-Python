'''

49. Group Anagrams
Medium

5268

229

Add to List

Share
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.

'''

class Solution:
    
    def group(self,s,h):
        
        for i in h:
            if not set(i)^set(s):
                h[i].append(s)
                return
        
        h[s] = []
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        
        for i in strs:
            self.group(i,h)
            
        print(h)
        res = []    
        for j in h:
            res.append([j]+h[j])
            
        return res
        
