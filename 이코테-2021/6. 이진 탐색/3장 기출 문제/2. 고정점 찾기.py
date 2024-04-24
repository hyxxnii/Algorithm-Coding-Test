import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

def binary_search(start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if mid == data[mid]:
        return mid
    elif mid > data[mid]:
        return binary_search(mid + 1, end)
    elif mid < data[mid]:
        return binary_search(start, mid - 1)

ans = binary_search(0, N - 1)
if ans == None:
    print("-1")
else:
    print(ans)