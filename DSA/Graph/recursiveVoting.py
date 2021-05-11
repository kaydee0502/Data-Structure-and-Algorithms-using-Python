'''

Recursive Voting
You are given a list of integers votes representing election votes for candidates a and b. Each element in votes represents a vote to one of the two candidates:

If votes[i] < 0, then it's a vote for a.
If votes[i] ≥ n, then it's a vote for b.
Otherwise, the vote at index i made the same vote as votes[votes[i]].
Return the number of votes that candidate a received. You can assume all votes are eventually made to either a or b.

Constraints

0 ≤ n ≤ 100,000 where n is the length of votes
Example 1
Input
votes = [2, -1, 5, 1, 3]
Output
3
Explanation
We can see that votes[1], votes[3], and votes[4] were made to candidate a.

'''

class Solution:
    def solve(self, votes):
        par= [-1] * len(votes)

        for i in range(len(votes)):
            if votes[i] < 0:
                par[i] = "a"
            if votes[i] >= len(votes):
                par[i] = "b"



        def find(x):
            nonlocal par
            nonlocal votes
            if par[x] != -1:
                return par[x]

            f = find(votes[x])
            par[x] = f
            return f

        for i in range(len(par)):
            if par[i] == -1:
                find(i)
                
        aas = 0
        for i in par:
            if i == "a":
                aas+=1

        return aas