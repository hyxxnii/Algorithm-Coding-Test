# https://www.acmicpc.net/problem/20365

import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().rstrip())

cnt = [0, 0]
compare, i = arr[0], 0
for j in range(n):
    if compare != arr[j]:
        cnt[i%2] += 1
        compare = arr[j]
        i += 1
        
cnt[i%2] += 1

print(min(cnt) + 1)