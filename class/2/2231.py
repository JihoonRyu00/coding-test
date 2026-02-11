# 2231.py
# 분해합
# https://www.acmicpc.net/problem/2231

import sys
input=sys.stdin.readline

N=input().rstrip()
len_n=len(N)
first=int(N[0])
N=int(N)

curr=max(1,N-(9*(len_n-1)+first))
while curr<N:    
    if curr+sum(map(int,str(curr)))==N:
        print(curr)
        sys.exit()
    curr+=1
print(0)