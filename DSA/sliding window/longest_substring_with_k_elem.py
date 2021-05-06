from collections import deque 
class Solution:
    def solve(self, k, nums):
        rw = deque()
        rwh = {}

        i = 0
        j = 0

        msize = 0
        while i<len(nums):
            

            if len(rwh) > k:
                v = rw.popleft()
                rwh[v] -= 1
                if rwh[v] == 0:
                    del rwh[v]

                j+=1
            
            else:
                rw.append(nums[i])
                if not nums[i] in rwh:
                    rwh[nums[i]] = 0

                rwh[nums[i]] += 1
                i+=1

            
            if len(rwh) <= k:
                #print(rwh,i,j)
                msize = max(msize,i-j)

        return msize