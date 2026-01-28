# 10951.py
# A+B - 4
# https://www.acmicpc.net/problem/10951

import sys
# input=sys.stdin.readline

# while True:
#     try:
#         A,B=map(int,input().split())
#         print(A+B)
#     except:
        # break

lines=sys.stdin.readlines()
for line in lines:
    A,B=map(int,line.split())
    print(A+B)