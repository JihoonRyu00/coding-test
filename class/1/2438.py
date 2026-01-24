# 2438.py
# 별 찍기 - 1
# https://www.acmicpc.net/problem/2438

N=int(input())
# for i in range(N):
#     for j in range(i+1):
#         print('*',end='')
#     print()
for i in range(N):
    print('*'*(i+1))