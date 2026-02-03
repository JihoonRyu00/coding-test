# 30802.py
# 웰컴 키트
# https://www.acmicpc.net/problem/30802

import sys
input=sys.stdin.readline

N=int(input())
sizes=list(map(int,input().split()))
T,P=map(int,input().split())

print(sum([(size-1)//T+1 for size in sizes]))
print(N//P,N%P)