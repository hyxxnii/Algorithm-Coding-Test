# https://www.acmicpc.net/problem/15721
import sys
input = sys.stdin.readline

a = int(input())
t = int(input())
q = int(input()) # 0 / 1
bundegi = []

# % a
i = 1 # 게임 회차
bun = degi = 1
while True:
    for _ in range(2): # 0 1 0 1
        bundegi.append((bun, 0))
        bun += 1
        bundegi.append((degi, 1))
        degi += 1
    for _ in range(i+1): # 0 *(n+1)
        bundegi.append((bun, 0))
        bun += 1
    for _ in range(i+1): # 1 *(n+1)
        bundegi.append((degi, 1))
        degi += 1
    
    i += 1
    if bun >= t:
        find = bundegi.index((t, q))
        print(find % a)
        break