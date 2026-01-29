# 2439.py
# 별 찍기 - 2
# https://www.acmicpc.net/problem/2439

import sys
input=sys.stdin.readline

N=int(input())
for i in range(1,N+1):
    print(' '*(N-i)+'*'*i)