import sys
input = sys.stdin.readline

n = int(input())
res = list([int(input()) for _ in range(n)])
res.sort()
cnt = res[0]
result = 0
for i in range(1, n):
    cnt += res[i]
    result += cnt
print(result)

## 우선순위 큐 이용
n = int(input())
# res.sort()
import heapq
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

result = 0
while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_ = one + two
    result += sum_
    heapq.heappush(heap, sum_)
    
print(result)