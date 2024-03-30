# https://www.acmicpc.net/problem/1789
import sys

input = sys.stdin.readline
s = int(input())

i = 0
cnt = 0
while True:
    if s > i:
        i += 1
        s -= i
        cnt += 1
    else:
        print(cnt)
        break