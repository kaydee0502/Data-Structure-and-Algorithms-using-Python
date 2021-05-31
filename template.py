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

t = int(input())

while t:
    n,k = map(int,input().split())
    s = input()
    qs = list(map(int,input().split()))
    
    
    pre = []
    
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            pre.append(2)
        else:
            pre.append(1)
            
    csum = sum(pre)
    s= list(s)
    
    for i in qs:
        i = i-1
        nex = i
        prev = i-1
        
        s[i] = "0" if s[i] == "1" else "1"
        #print(s,nex,prev)
        if i > 0:
            if s[i] == s[i-1]:
                csum+=1
            else:
                csum-=1
                
        if i < n-1:
            if s[i] == s[i+1]:
                csum+=1
            else:
                csum-=1
                
        print(csum)
            
        
            
        
    
    
    t-=1