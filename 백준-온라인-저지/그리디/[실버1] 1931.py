# https://www.acmicpc.net/problem/1931

## 1. 우선순위 큐
import heapq

n = int(input())
res = 0
time = 0 # 회의 종료 후 현재 시간

q = [] # 우선순위 큐
for _ in range(n):
    s, e = map(int, input().split())
    heapq.heappush(q, (e, s)) # 빨리 끝나는 순

for i in range(len(q)):
    e, s = heapq.heappop(q)
    if time <= s:
        time = e
        res += 1
        
print(res)


## 2. 리스트, 정렬 함수
n = int(input())
res = 0
time = 0

data = []
for _ in range(n):
    s, e = map(int, input().split())
    data.append((e, s))

data = sorted(data) # 종료 시간이 빠른 순으로 정렬

for e, s in data:
    if time <= s:
        time = e
        res += 1
        
print(res)