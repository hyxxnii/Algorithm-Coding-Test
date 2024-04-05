# https://www.acmicpc.net/problem/11508

import sys
input = sys.stdin.readline

n = int(input())
data = list([int(input()) for _ in range(n)])
data.sort(reverse=True)

total = sum(data)
for i in range(2, n, 3):
    total -= data[i]
print(total)