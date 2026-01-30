# 3052.py
# 나머지
# https://www.acmicpc.net/problem/3052

import sys
input=sys.stdin.readline

print(len({int(input().rstrip())%42 for _ in range(10)}))
# print(len(set([int(input().rstrip())%42 for _ in range(10)])))