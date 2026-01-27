# 10950.py
# A+B - 3
# https://www.acmicpc.net/problem/10950

import sys
input=sys.stdin.readline

N=int(input())
for _ in range(N):
    A,B=map(int,input().split())
    print(A+B)