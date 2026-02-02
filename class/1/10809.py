# 10809.py
# 알파벳 찾기
# https://www.acmicpc.net/problem/10809

import sys
input=sys.stdin.readline

S=input()
for i in range(26):
    print(S.find(chr(i+ord('a'))),end=' ')