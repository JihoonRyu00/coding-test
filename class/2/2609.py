# 2609.py
# 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609

import sys
input=sys.stdin.readline

# 재귀
def get_gcd(a,b):
    if b==0:
        return a
    return get_gcd(b,a%b)

# 반복
# def get_gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

A,B=map(int,input().split())
gcd=get_gcd(A,B)
print(gcd,A*B//gcd,sep='\n')