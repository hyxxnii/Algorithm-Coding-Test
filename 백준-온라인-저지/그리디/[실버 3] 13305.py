n = int(input())
dist = list(map(int, input().split())) # [2, 3, 1]
cost = list(map(int, input().split())) # [5, 2, 4, 1]

now = cost[0]
result = 0
for i in range(n-1):
    if now > cost[i]:
        now = cost[i]
    result += now * dist[i]
    
print(result)