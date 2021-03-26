class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def peek(self):
        if not self.top:
            return
        else:
            return self.top.val
    
    def push(self,val):
        newnode = Node(val)
        if self.length == 0:
            self.top = newnode
            self.bottom = newnode
            
        else:
            temp = self.top
            self.top = newnode
            self.top.next = temp

        self.length+=1

            
    def pop(self):
         if self.top == None:
             return
         else:
             temp = self.top
             self.top = self.top.next
             self.length -= 1
         return temp.val
            

myStck = Stack()
myStck.push('Google')

myStck.push('Amazon')
myStck.push('Alibaba')
print(myStck.pop())
print(myStck.peek())
myStck.push('Azure')
print(myStck.peek())



