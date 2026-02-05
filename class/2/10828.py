# 10828.py
# 스택
# https://www.acmicpc.net/problem/10828

import sys
input=sys.stdin.readline

N=int(input())
stack=[]
for _ in range(N):
    com=input().split()
    if com[0]=='push':
        stack.append(com[1])
    elif com[0]=='pop':
        print(stack.pop() if stack else -1)
    elif com[0]=='size':
        print(len(stack))
    elif com[0]=='empty':
        print(1 if not stack else 0)
    elif com[0]=='top':
        print(stack[-1] if stack else -1)