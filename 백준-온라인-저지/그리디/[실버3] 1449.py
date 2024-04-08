# https://www.acmicpc.net/problem/1449

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = 1
start = arr[0]

for data in arr[1:]:
    if data in range(start, start + l):
        continue
    else:
        result += 1
        start = data
        
print(result)