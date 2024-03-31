# https://www.acmicpc.net/problem/19637
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
#name, power = [], []
chingho = [input().split() for _ in range(n)] # 오름차순
targets = [int(input().rstrip()) for _ in range(m)]

for target in targets:
    start = 0
    end = n - 1
    result = 0
    # min_ = 1e9
    while start <= end:
        mid = (start + end) // 2
        if target <= int(chingho[mid][1]):
            result = chingho[mid][0]
            end = mid - 1
        else:
            start = mid + 1
        
    print(result)
