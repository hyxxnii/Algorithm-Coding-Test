# https://www.acmicpc.net/problem/17413
import sys
input = sys.stdin.readline

S = input().rstrip()
result = ""
stack = []
opened = 0
for i in S:
    if i == "<":
        for _ in range(len(stack)):
            result += stack.pop()
        opened = 1 # 괄호 시작

    if opened == 1: # 괄호 안이라면
        result += i
        if i == ">":
            opened = 0 # 괄호 끝
            continue
    
    if opened == 0 and i == " ":
        for _ in range(len(stack)):
            result += stack.pop()
        result += i
    
    elif opened == 0:
        stack.append(i)

if stack:
    for _ in range(len(stack)):
        result += stack.pop()
print(result)
