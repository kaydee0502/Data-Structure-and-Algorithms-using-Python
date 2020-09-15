#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    n = n*k
    l = len(n)
    def tem(n,l):
        if l == 0:
            return 0
        #print(n[k-1])
        return tem(n,l-1) + int(n[l-1])
        print(5)
    a = tem(n,l)
    while len(str(a)) != 1:
        a = tem(str(a),len(str(a)))

    return a

    

if __name__ == '__main__':
    

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)
    print(result)

    

    
