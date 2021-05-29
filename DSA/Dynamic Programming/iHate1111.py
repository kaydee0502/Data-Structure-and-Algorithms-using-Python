'''

B. I Hate 1111
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given an integer x. Can you make x by summing up some number of 11,111,1111,11111,…? (You can use any number among them any number of times).

For instance,

33=11+11+11
144=111+11+11+11
Input
The first line of input contains a single integer t (1≤t≤10000) — the number of testcases.

The first and only line of each testcase contains a single integer x (1≤x≤109) — the number you have to make.

Output
For each testcase, you should output a single string. If you can make x, output "YES" (without quotes). Otherwise, output "NO".

You can print each letter of "YES" and "NO" in any case (upper or lower).

Example
input
3
33
144
69
output
YES
YES
NO
Note
Ways to make 33 and 144 were presented in the statement. It can be proved that we can't present 69 this way.


'''

"""                                    

╭╮╭━╮╱╱╱╱╱╱╭━━━╮
┃┃┃╭╯╱╱╱╱╱╱╰╮╭╮┃
┃╰╯╯╭━━┳╮╱╭╮┃┃┃┣━━┳━━╮
┃╭╮┃┃╭╮┃┃╱┃┃┃┃┃┃┃━┫┃━┫
┃┃┃╰┫╭╮┃╰━╯┣╯╰╯┃┃━┫┃━┫
╰╯╰━┻╯╰┻━╮╭┻━━━┻━━┻━━╯
╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╰━━╯
"""
import sys, io, os

BUFSIZE = 8192


class FastIO(io.IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = io.BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(io.IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
# endregion


T = int(input())


dp = {}

def rec(n,s):
    if n == 0:
        #print("OK")
        return True
    
    if n < 11 or len(s) < 2:
        return False
        
    
    if n < int(s) and len(s) == 2:
        return False
    
    
    
    
    if (n,s) in dp:
        return dp[(n,s)]
    
    if n >= int(s):
        #print(n,s)
        dp[(n,s)] = rec(n-int(s),s) or rec(n,s[:-1])
    else:
        dp[(n,s)] = rec(n,s[:-1])
    return dp[(n,s)]
     
    
    

# def knapSack(self, N, W, val, wt):
    
    

        
#         dp = [[0 for i in range(W+1)] for j in range(N+1)]
        
#         for i in range(1,N+1):
#             for j in range(1,W+1):
#                 if j>=wt[i-1]:
#                     dp[i][j] = max(val[i-1]+dp[i][j-wt[i-1]],dp[i-1][j])
#                 else:
#                     dp[i][j] = dp[i-1][j]
                    
                    
#         #print(dp)
#         return dp[-1][-1]

while T:
    n = int(input())
  
    s = "1"*(len(str(n))+1)
    
    if n < 11:
        print("NO")
        T-=1
        continue
    
    if rec(n,s):
        print("YES")
    else:
        print("NO")

     
     
     
  
        
    T-=1