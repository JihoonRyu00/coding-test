# 8958.py
# OX퀴즈
# https://www.acmicpc.net/problem/8958

import sys
input=sys.stdin.readline

T=int(input())
# for _ in range(T):
#     score=0
#     stacked=0
#     ans=input().rstrip()
#     for a in ans:
#         if a=='O':
#             stacked+=1
#             score+=stacked
#         elif a=='X':
#             stacked=0
#     print(score)
for _ in range(T):
    ans=input().rstrip()
    print(sum(len(a)*(len(a)+1)//2 for a in ans.split('X')))