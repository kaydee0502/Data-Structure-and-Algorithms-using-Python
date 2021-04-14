'''


Job Sequencing Problem
Medium Accuracy: 48.94% Submissions: 13324 Points: 4

Given a set of N jobs where each job i has a deadline and profit associated to it. Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit if and only if the job is completed by its deadline. The task is to find the maximum profit and the number of jobs done.

Note: Jobs will be given in the form (Job id, Deadline, Profit) associated to that Job.


Example 1:

Input:
N = 4
Jobs = (1,4,20)(2,1,10)(3,1,40)(4,1,30)
Output:
2 60
Explanation:
2 jobs can be done with
maximum profit of 60 (20+40).

Example 2:

Input:
N = 5
Jobs = (1,2,100)(2,1,19)(3,2,27)
(4,1,25)(5,1,15)
Output:
2 127
Explanation:
2 jobs can be done with
maximum profit of 127 (100+27).


Your Task :
You don't need to read input or print anything. Your task is to complete the function JobScheduling() which takes an Integer N and an array of Jobs(Job id, Deadline, Profit) as input and returns the count of jobs and maximum profit.


Expected Time Complexity: O(NlogN)
Expected Auxilliary Space: O(N)


Constraints:
1 <= N <= 100000
1 <= Deadline <= 100
1 <= Profit <= 500

'''

#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        Jobs.sort(key = lambda x : x.profit,reverse =True)
        #print(Jobs[0].profit)
        
        dead = 0
        job = 0
        
        dead = max(Jobs,key = lambda x : x.deadline)
        profit = 0
        slots = [-1] * dead.deadline
        fills = dead.deadline
        
        for i in Jobs:
            
            if fills <= 0:
                break
            j = i.deadline-1
            
            while j > -1:
                if slots[j] == -1:
                    break
                
                j-=1
            else:
                continue
            
            slots[j] = i.id
            profit += i.profit
            job+=1
            fills-=1
        
        
        return [job,profit]
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends

