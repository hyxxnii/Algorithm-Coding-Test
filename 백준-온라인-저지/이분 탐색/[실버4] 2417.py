# https://www.acmicpc.net/problem/2417
import sys
input = sys.stdin.readline

n = int(input())

start = 0
end = n
result = n
while start <= end:
    mid = (start + end) // 2
    if mid**2 >= n:
        result = min(result, mid)
        end = mid - 1
    elif mid**2 < n:
        start = mid + 1

print(result)