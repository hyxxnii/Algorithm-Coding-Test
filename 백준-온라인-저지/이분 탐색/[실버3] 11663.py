# https://www.acmicpc.net/problem/11663
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dots = list(map(int, input().split()))
dots.sort()

# 선분 시작점 구하기
def dot_start(target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if target == dots[mid]:
            return mid
        elif target < dots[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end + 1
            
# 선분 끝점 구하기
def dot_end(target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if target == dots[mid]:
            return mid
        elif target < dots[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end

for _ in range(m):
    s, e = map(int, input().split())
    # print(dot_end(e), dot_start(s))
    print(dot_end(e) - dot_start(s) + 1)