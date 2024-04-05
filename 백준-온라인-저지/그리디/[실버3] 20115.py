# https://www.acmicpc.net/problem/20115

n = int(input())
drink = list(map(int, input().split()))

drink.sort()

res = drink[-1]
for d in drink[:-1]:
    res += d / 2

print(res)