# 4153.py
# 직각삼각형
# https://www.acmicpc.net/problem/4153

import sys
# input=sys.stdin.readline

lines=sys.stdin.readlines()
for line in lines:
    a,b,c=sorted(list(map(int,line.split())))
    if a==0:
        sys.exit()
    if c**2==a**2+b**2:
        print('right')
    else:
        print('wrong')