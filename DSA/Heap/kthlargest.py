'''

703. Kth Largest Element in a Stream
Easy

1195

731

Add to List

Share
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Returns the element representing the kth largest element in the stream.
 

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
 

Constraints:

1 <= k <= 10^4
0 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
-10^4 <= val <= 10^4
At most 10^4 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.


'''

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        heapq.heapify(self.heap)
        
        
        for i in nums:
            #print(self.heap)
            if len(self.heap) < k:
                heapq.heappush(self.heap,i)
            else:
                if i > self.heap[0]:
                    heapq.heappushpop(self.heap,i)
                
        

    def add(self, val: int) -> int:
        
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
        else:
            heapq.heappushpop(self.heap,val)
        
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
