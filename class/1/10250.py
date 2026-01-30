# 10250.py
# ACM 호텔
# https://www.acmicpc.net/problem/10250

import sys
input=sys.stdin.readline

T=int(input())
for t in range(T):
    H,W,N=map(int,input().split())
    XX=(N-1)%H+1
    YY=(N-1)//H+1
    print(XX*100+YY)