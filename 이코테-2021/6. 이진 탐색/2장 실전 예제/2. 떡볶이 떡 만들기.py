import sys
input = sys.stdin.readline

# 전형적인 이진 탐색 문제 => 파라메트릭 서치(Parametric Search) 유형의 문제
# 파라메트릭 서치: 최적화 문제를 결정 문제로 바꾸어 해결하는 법
# 원하는 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제 => 이진 탐색으로 결정 문제를 해결하면서 범위 좁혀 나갈 수 있음

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    result = -1
    while start <= end:
        mid = (start + end) // 2
        cum = 0
        for i in arr:
            if mid < i:
                cum += (i - mid)
        
        if cum < target:
            end = mid -1
        else:
            result = mid
            start = mid + 1
    return result
# end = 19
# start = 0

result = binary_search(arr, m, 0, max(arr))
print(result)