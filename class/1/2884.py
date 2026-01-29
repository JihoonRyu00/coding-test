# 2884.py
# 알람 시계
# https://www.acmicpc.net/problem/2884

import sys
input=sys.stdin.readline

H,M=map(int,input().split())
# if M<45:
#     H=H-1
# print(H%24,(M-45)%60)
total=H*60+M-45
print(total//60%24,total%60)