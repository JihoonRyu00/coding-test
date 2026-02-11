# 1874.py
# 스택 수열
# https://www.acmicpc.net/problem/1874

import sys
input=sys.stdin.readline

n=int(input())
cmd=[]
stack=[]
curr=1
possible=True
for _ in range(n):
    num=int(input())
    while curr<=num:
        stack.append(curr)
        cmd.append('+')
        curr+=1
    if stack[-1]!=num:
        possible=False
        break
    stack.pop()
    cmd.append('-')
if possible:
    print('\n'.join(cmd))
else:
    print('NO')