class node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    
    def hnt(self,head):
        h = head
        t = head
        prop = True
        while h != t or prop:
            h = h.next
            t = t.next.next
            prop = False
            
        loop_size = 0
        prop = True
        
        while h != t or prop:
            prop = False
            t = t.next
                
            loop_size += 1
            
        h = head
        t = head
        
        for i in range(loop_size):
            t = t.next
        
        
        
        while 1:
            #print(h.val,t.val)
            if h.val == t.val:
                return h.val
            h = h.next
            t = t.next
            
        return h.val
        
        
    def chk(self,head):
        h = head
        t = head
        h = h.next
        t = t.next.next
        
        
        while h != t:
            print("ye")
            h = h.next
            t = t.next.next
    
    def findDuplicate(self, nums) -> int:
        for i in range(len(nums)):
            nums[i] = node(nums[i])
            
        for j in range(len(nums)):
            nums[j].next = nums[nums[j].val]
                
                
        return self.hnt(nums[0])
                
            
s = Solution()

print(s.findDuplicate([1,3,4,2,2]))
        