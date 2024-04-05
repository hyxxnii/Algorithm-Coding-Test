# https://www.acmicpc.net/problem/16208

import sys
input = sys.stdin.readline

n = int(input())
stick = list(map(int, input().split()))
stick.sort()

sum_ = sum(stick)
result = 0
for i in range(n):
    sum_ -= stick[i]
    result += sum_ * stick[i]

print(result)