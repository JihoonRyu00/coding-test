# 2839.py
# 설탕 배달
# https://www.acmicpc.net/problem/2839

import sys
input=sys.stdin.readline

N=int(input())

# dp
# dp=[float('inf')]*(N+1)
# if N>=3:
#     dp[3]=1
# if N>=5:
#     dp[5]=1
# for i in range(6,N+1):
#     dp[i]=min(dp[i-3],dp[i-5])+1
# print(dp[N] if dp[N]!=float('inf') else -1)

# greedy
result=0
while True:
    if N%5==0:
        result+=N//5
        break
    if N<3:
        result=-1
        break
    N-=3
    result+=1
print(result)