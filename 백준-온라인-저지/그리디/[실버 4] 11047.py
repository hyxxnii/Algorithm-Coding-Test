n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

result = 0
for x in coins[::-1]:
    if x <= k:
        cnt= k // x
        k -= x * cnt
        result += cnt
        
print(result)