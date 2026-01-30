# 2675.py
# 문자열 반복
# http://acmicpc.net/problem/2675

import sys
input=sys.stdin.readline

T=int(input())
for t in range(T):
    R,S=input().split()
    # print(*[s*int(R) for s in S],sep='')
    print("".join(s*int(R) for s in S))