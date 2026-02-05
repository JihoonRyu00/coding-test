# 4949.py
# 균형잡힌 세상
# https://www.acmicpc.net/problem/4949

import sys
input=sys.stdin.readline

while True:
    line=input().rstrip()
    if line=='.':
        break
    stack=[0]
    is_balanced=True
    for l in line:
        if l=='(' or l=='[':
            stack.append(l)
        elif l==')':
            if stack[-1]=='(':
                stack.pop()
            else:
                is_balanced=False
                break
        elif l==']':
            if stack[-1]=='[':
                stack.pop()
            else:
                is_balanced=False
                break
    print('yes' if is_balanced and len(stack)==1 else 'no')


# import sys
# input = sys.stdin.readline

# while True:
#     line = input().rstrip()
#     if line == '.':
#         break
    
#     stack = []
#     is_balanced = True
    
#     for l in line:
#         if l in '([':
#             stack.append(l)
            
#         elif l == ')':
#             if not stack or stack.pop() != '(':
#                 is_balanced = False
#                 break
                
#         elif l == ']':
#             if not stack or stack.pop() != '[':
#                 is_balanced = False
#                 break
                
#     if is_balanced and not stack:
#         print("yes")
#     else:
#         print("no")