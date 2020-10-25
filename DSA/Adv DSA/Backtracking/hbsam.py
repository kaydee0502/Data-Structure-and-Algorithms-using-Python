from itertools import permutations
for _ in range(int(input())):
    n,a,b,c = map(int,input().split())
    arr = [i for i in range(1,n+1-c+1)]
    for i in range(c-1):
        arr.append(arr[-1])
    perm = permutations(arr)
    
    for i in perm:
        counta = 0
        countb = 0
        lmax = -1
        gmax = -1
        flag = True
        m = max(i)
        for j in range(n):
            if lmax == -1:
                lmax = i[j]
                counta += 1
            elif i[j] > lmax or i[j] == m:
                counta += 1
                lmax = i[j]
        for j in range(n-1,-1,-1):
            if gmax == -1:
                gmax = i[j]
                countb += 1
            elif i[j] > gmax or i[j] == m:
                countb += 1
                gmax = i[j]
        if counta == a and countb == b:
            flag = False
            break
    if flag:
        print("Case #{}: IMPOSSIBLE".format(_+1))
    else:
        print("Case #{}:".format(_+1),*i)