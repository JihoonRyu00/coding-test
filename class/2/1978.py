# 1978.py
# 소수 찾기
# https://www.acmicpc.net/problem/1978

N=int(input())

# 1000 이하 소수
limit=1000
is_prime=[True]*(limit+1)
is_prime[0]=is_prime[1]=False
for i in range(1,int(limit**0.5)+1):
    if is_prime[i]:
        is_prime[i*i::i]=[False]*len(is_prime[i*i::i])

print(sum(is_prime[num] for num in map(int,input().split())))
