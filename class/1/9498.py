# 9498.py
# 시험 성적
# https://www.acmicpc.net/problem/9498

# score=int(input())
# if score>=90:
#     print('A')
# elif score>=80:
#     print('B')
# elif score>=70:
#     print("C")
# elif score>=60:
#     print("D")
# else:
#     print("F")
def solve():
    score=int(input())
    if score>=90:
        print('A')
        return
    if score>=80:
        print('B')
        return
    if score>=70:
        print("C")
        return
    if score>=60:
        print("D")
        return
    print("F")

solve()