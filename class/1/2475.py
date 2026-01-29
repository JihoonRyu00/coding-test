# 2475.py
# 검증수
# https://www.acmicpc.net/problem/2475

import sys
input=sys.stdin.readline

nums=list(map(int,input().split()))
print(sum([num**2 for num in nums])%10)