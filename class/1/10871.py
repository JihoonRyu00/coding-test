# 10871.py
# X보다 작은 수
# https://www.acmicpc.net/problem/10871

N,X=map(int,input().split())
nums=list(map(int, input().split()))
# result=[]
# for l in nums:
#     if l<X:
#         result.append(l)
result = [n for n in nums if n < X]
print(*result)