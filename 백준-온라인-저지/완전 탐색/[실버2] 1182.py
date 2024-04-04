# https://www.acmicpc.net/problem/1182

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))

def solve(start, total):
    global cnt
    if start == n:
        return
    
    total += data[start]
    if total == s:
        cnt += 1
        
    for r in range(start+1, n):
        solve(r, total)
        
cnt = 0
total = 0
for i in range(n):
    solve(i, total)
print(cnt)