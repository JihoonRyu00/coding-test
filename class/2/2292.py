# 2292.py
# 벌집
# https://www.acmicpc.net/problem/2292

import sys
input=sys.stdin.readline

N=int(input())
count=0
while N>0:
    N-=max(1,6*count)
    count+=1
print(count)