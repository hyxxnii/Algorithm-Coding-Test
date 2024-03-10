# https://www.acmicpc.net/problem/1913
n = int(input())
find = int(input())
find_s = find_e = (n // 2) + 1

table = [list([0] * n) for _ in range(n)]

s = e = n // 2
table[s][e] = 1
i = 2

start_n = 3

while True:    
    if start_n > n:
        break
    
    # 상 1번
    s -= 1
    table[s][e] = i
    if i == find:
        find_s = s + 1
        find_e = e + 1
    i += 1
    
    # 우 (n-2)번
    for _ in range(start_n-2):
        e += 1
        table[s][e] = i
        if i == find:
            find_s = s + 1
            find_e = e + 1
        i += 1
    
    # 하 (n-1) 번
    for _ in range(start_n-1):
        s += 1
        table[s][e] = i
        if i == find:
            find_s = s + 1
            find_e = e + 1
        i += 1
    
    # 좌 (n-1) 번
    for _ in range(start_n-1):
        e -= 1
        table[s][e] = i
        if i == find:
            find_s = s + 1
            find_e = e + 1
        i += 1
    
    # 상 n-1 번
    for _ in range(start_n-1):
        s -= 1
        table[s][e] = i
        if i == find:
            find_s = s + 1
            find_e = e + 1
        i += 1
        
    start_n += 2

for i in range(n):
    print(*table[i])
    
print(find_s, find_e)