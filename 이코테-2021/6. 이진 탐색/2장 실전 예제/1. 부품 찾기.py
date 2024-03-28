import sys
input = sys.stdin.readline

n = int(input())
parts = list(map(int, input().split()))
m = int(input())
finds = list(map(int, input().split()))

# 있으면 yes, 없으면 no
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return "yes"
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return "no"

parts.sort()
for i in finds:
    result = binary_search(parts, i, 0, n-1)
    print(result, end=' ')