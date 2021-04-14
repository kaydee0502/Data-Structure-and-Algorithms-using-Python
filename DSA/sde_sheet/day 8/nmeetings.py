'''


N meetings in one room
Easy Accuracy: 43.1% Submissions: 15450 Points: 2

There is one meeting room in a firm. There are N meetings in the form of (S[i], F[i]) where S[i] is start time of meeting i and F[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time? Also note start time of one chosen meeting can't be equal to the end time of the other chosen meeting.


Example 1:

Input:
N = 6
S[] = {1,3,0,5,8,5}
F[] = {2,4,6,7,9,9}
Output: 
4
Explanation:
Four meetings can be held with
given start and end timings.

Example 2:

Input:
N = 8
S[] = {75250, 50074, 43659, 8931, 11273,
27545, 50879, 77924}
F[] = {112960, 114515, 81825, 93424, 54316,
35533, 73383, 160252}
Output: 
3
Explanation:
Only three meetings can be held
with given start and end timings.


Your Task :
You don't need to read inputs or print anything. Complete the function maxMeetings() that recieves array S[ ] and F[ ] along with their size N as input parameters and returns the maximum number of meetings that can be held in the meeting room.


Expected Time Complexity : O(N*LogN)
Expected Auxilliary Space : O(N)


Constraints:
1 ≤ N ≤ 10^5
0 ≤ S[i] < F[i] ≤ 10^5

'''


#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        
        z = list(zip(end,start))
        
        z.sort()
        
        end, start = zip(*z)
        
        st = start[0]
        en = end[0]
        
        c = 1
        
        for i,j in zip(start,end):
            if i > en:
                st = i
                en = j
                c+=1
                
        return c
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends
