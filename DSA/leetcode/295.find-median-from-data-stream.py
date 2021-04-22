#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []
        self.n = 0
        self.k = 0
        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)
        

    def addNum(self, num: int) -> None:
        if len(self.minheap) == len(self.maxheap):
            heapq.heappush(self.maxheap,-heapq.heappushpop(self.minheap,-num))
        else:
            heapq.heappush(self.minheap,-heapq.heappushpop(self.maxheap,num))
        
       

    def findMedian(self) -> float:
        #print(self.minheap,self.maxheap)
        
        if len(self.minheap)== len(self.maxheap):
            
            return ((self.maxheap[0])-self.minheap[0])/2
        else:
            return self.maxheap[0]
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

