n = int(input())
seq = input()

got_pc = set()
pc_nhi_mila_vro = set()
leftout = 0

for i in seq:
    if i in got_pc:
        got_pc.discard(i)
    elif i in pc_nhi_mila_vro:
        pc_nhi_mila_vro.discard(i)
        
    elif len(got_pc) >= n:
        leftout += 1
        pc_nhi_mila_vro.add(i)
        
    else:
        got_pc.add(i)
        
print(leftout)
    
        