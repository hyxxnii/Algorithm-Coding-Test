# https://www.acmicpc.net/problem/10815
import sys

input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))
card.sort() # -10 2 3 6 10
m = int(input())
find = list(map(int, input().split()))

for i in find:
    start = 0
    end = n-1
    ret = 0
    while start <= end:
        mid = (start + end) // 2        
        if card[mid] == i:
            ret = 1
            break
        elif card[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    print(ret, end=' ')