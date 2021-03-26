class Solution:
    def calculateSpan(self,a,n):
        stack = []
        spans = []
        for i in range(n):
            
            if not stack:
                spans.append(1)
            else:
                while stack:
                    if stack[-1][0] > a[i]:
                        spans.append(i - stack[-1][1])
                        break
                    stack.pop()
                else:
                    spans.append(i+1)
            stack.append([a[i],i])
        return spans


sol = Solution()
print(sol.calculateSpan([100,80,60,70,60,75,85],7))