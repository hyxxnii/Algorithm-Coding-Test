# https://www.acmicpc.net/problem/20300

n = int(input())
data = list(map(int, input().split()))

data.sort()
res = [0] * (n // 2)

if len(data) % 2 != 0:
    res.append(data[-1])
    data.pop(-1)

for i in range(len(data) // 2):
        res[i] = data[i] + data[-i-1]

print(max(res))