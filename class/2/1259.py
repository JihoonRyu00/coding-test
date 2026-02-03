# 1259.py
# 팰린드롬수
# https://www.acmicpc.net/problem/1259

import sys
input=sys.stdin.readline

def is_palindrome(word):
    # n=len(word)
    # for i in range(n//2):
    #     if word[i]!=word[n-1-i]:
    #         return False
    # return True
    if word==word[::-1]:
        return True
    else:
        return False

while True:
    line=input().rstrip()
    if line=="0":
        break
    print("yes" if is_palindrome(line) else "no")