
def solve2(i,s,temp_res):
    if i == -1:
        return
    
    solve2(i-1,s[:i],temp_res)
    
    temp_res.append(s)
    
    


def solve(i,n,s,final_res):
    
    if i == n:
        return
    
    temp_res = []
    solve2(len(s[i:])-1,s[i:],temp_res)
    final_res.append(temp_res)
    
    solve(i+1,n,s,final_res)



final_res = []
s = "abcd"

solve(0,len(s),s,final_res)

for i in final_res:
    print(",".join(i))