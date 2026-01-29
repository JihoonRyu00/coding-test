# 2562.py
# 최댓값
# https://www.acmicpc.net/problem/2562

import sys
input=sys.stdin.readline

# max_num=0
# max_i=0
# for i in range(1,10):
#     n=int(input())
#     if n>max_num:
#         max_num=n
#         max_i=i
# print(f"{max_num}\n{max_i}")

nums=[int(input()) for _ in range(9)]
print(max(nums))
print(nums.index(max(nums))+1)