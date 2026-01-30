# 2920.py
# 음계
# https://www.acmicpc.net/problem/2920

import sys
input=sys.stdin.readline

melodies="".join(input().split())
# if melodies=="12345678":
#     print("ascending")
# elif melodies=="87654321":
#     print("descending")
# else:
#     print("mixed")

answers={"12345678":"ascending",
        "87654321":"descending"}
print(answers.get(melodies,"mixed"))