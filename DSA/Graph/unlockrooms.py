'''
Unlock Rooms
You are given a two-dimensional list of integers rooms. Each index i in rooms represents a room and rooms[i] represents different keys to unlock other rooms.

You are currently in an unlocked room 0 and every other room is locked. Given you can move freely between unlocked rooms, return whether you can unlock every room.

Constraints

n, m ≤ 250 where n and m are the number of rows and columns in rooms.
Example 1
Input
rooms = [
    [1, 3],
    [2],
    [0],
    []
]
Output
True
Explanation
We start off at room 0 and can go to room 1 with its key. From room 1 we can go to room 2. Then, we can go back to room 0 and go to room 3.

'''

from collections import defaultdict

class Solution:

    def __init__(self):
        self.g = defaultdict(list)

    def addE(self,u,v):
        self.g[u].append(v)

    def dfs(self,s,vis):
        vis[s] = True

        for i in self.g[s]:
            if vis[i] == False:
                self.dfs(i,vis)




    def solve(self, rooms):
        for i in range(len(rooms)):
            for j in rooms[i]:
                self.addE(i,j)

        n = len(rooms)
        vis = [False] * n

        self.dfs(0,vis)

        if sum(vis) == n:
            return True
        return False