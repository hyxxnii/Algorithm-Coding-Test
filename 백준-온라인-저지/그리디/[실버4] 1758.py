# https://www.acmicpc.net/problem/1758
import sys
input = sys.stdin.readline

n = int(input())
data = list([int(input()) for _ in range(n)])
data.sort(reverse=True)

total = 0
for i in range(len(data)):
    mid = data[i] - (i + 1 - 1)
    if mid > 0:
        total += mid
print(total)