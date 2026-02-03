# 2798.py
# 블랙잭
# https://www.acmicpc.net/problem/2798

import sys
input=sys.stdin.readline

N,M=map(int,input().split())
cards=list(map(int,input().split()))
result=0
cards.sort() # O(nlogn)

# 1 brute force + lookahead 최적화
for i in range(N-2):
    # 1. 최소 합 가지치기: 현재 i와 바로 뒤 2개를 더해도 M보다 크면 종료
    if cards[i]+cards[i+1]+cards[i+2]>M:
        break
    # 2. 최대 합 가지치기: 현재 i와 가장 큰 2개를 더해도 정답(result)보다 작으면 스킵
    if cards[i]+cards[N-1]+cards[N-2]<=result:
        continue
    for j in range(i+1,N-1):
        # 여기도 똑같이 적용 가능
        if cards[i]+cards[j]+cards[j+1]>M:
            break
        if cards[i]+cards[j]+cards[N-1]<=result:
            continue
        for k in range(j+1,N):
            curr_result=cards[i]+cards[j]+cards[k]
            if curr_result>M:
                break
            result=max(result,curr_result)
print(result)

# 2 two pointers
def tp(cards):
    result=sum(cards[:2])
    for i in range(N-2):
        curr_result=0
        left=i+1
        right=N-1
        while left<right:
            curr_result=cards[i]+cards[left]+cards[right]
            if curr_result<=M:
                # M을 넘지 않아야 하기 때문에 여기서 curr_result 저장해둬야 함
                # while문이 끝나고 저장하면 최종값만 남기 떄문에 중간과정 중에 생길 수 있는 최적값이 날아감
                result=max(curr_result,result)
                if result == M:
                    return M
                left+=1
            else:
                right-=1
    return result
print(tp(cards))