#User function Template for python3

def update( a, n, updates, k):
    #updates.sort()
    for i in range(k):
        updates[i] -= 1
        
    for i in updates:
        a[i] += 1
        
    for i in range(1,n):
        a[i] += a[i-1]
        
        
       
            
    # Your code goes here


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n , k = sz[0] , sz[1]
        a = [0 for i in range(n)]
        updates = [int(x) for x in input().strip().split()]
        update(a, n, updates, k)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
