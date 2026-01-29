# 2884.py
# 알람 시계
# https://www.acmicpc.net/problem/2884

import sys
input=sys.stdin.readline

def solve(H,M):
    if M>=45:
        print(H,M-45)
        return
    if H==0:
        H=24
    print(H-1,M+15)
    return
H,M=map(int,input().split())
solve(H,M)