# 2577.py
# 숫자의 개수
# https://www.acmicpc.net/problem/2577

import sys
input=sys.stdin.readline

A,B,C=[int(input().strip()) for _ in range(3)]
result=str(A*B*C)
# for i in range(0,10):
#     print(result.count(str(i)))
num_count=[0]*10
for r in result:
    num_count[int(r)]+=1
print(*num_count,sep='\n')