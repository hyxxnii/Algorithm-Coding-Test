# https://www.acmicpc.net/problem/14467

n = int(input())

ob = [-1] * 10
cnt = 0

for _ in range(n):
    a, b = map(int, input().split())
    
    if ob[a-1] == -1:
        ob[a-1] = b
        
    if ob[a-1] != b:
        ob[a-1] = b
        cnt += 1
    
print(cnt)