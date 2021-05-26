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
import sys
sys.setrecursionlimit(1000000)


def solve(x,y,mat,path,m,n,vis):
    global corners,di
    
    
    if x < 0 or y < 0 or x >= m or y >= n:
        return
    if vis[x][y]:
        return
    
    vis[x][y] = True
    
    if (x,y) in corners:
        path.append(mat[x][y])
        corners[(x,y)].append(path)
    
    
    
    for i,d in zip(di[(x,y)],((x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1),(x-1,y-1))):
        if i == 1:
            
            solve(d[0],d[i],mat,path+[mat[x][y]],m,n,vis)
            
    vis[x][y] = False
    
    
    
    
    
    




m,n,s = map(int,input().split())
corners = {(0,0):[],(0,n-1):[],(m-1,0):[],(m-1,n-1):[]}
mat = [[-1 for i in range(n)] for j in range(m)]
vis = [[False for i in range(n)] for j in range(m)]
di = {}
strt = None

for i in range(m*n):
    x = i // n
    y = i % n
    v, *dirs = list(map(int,input().split()))
    if v == s:
        strt = (x,y)
        
    di[(x,y)] = dirs
    mat[x][y] = v
    

solve(strt[0],strt[1],mat,[],m,n,vis)
print(*min(corners[(0,0)],key=len))
print(*min(corners[(0,n-1)],key=len))
print(*min(corners[(m-1,0)],key=len))
print(*min(corners[(m-1,n-1)],key=len))
    
    
        
    