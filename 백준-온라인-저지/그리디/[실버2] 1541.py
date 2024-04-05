# https://www.acmicpc.net/problem/1541

S = input()
data = S.split("-")

res = sum(map(int, data[0].split("+")))

for d in data[1:]:
    res -= sum(map(int, d.split("+")))

print(res)