# https://www.acmicpc.net/problem/14916

n = int(input())
cnt = 0

while n % 5 != 0:
    n -= 2
    cnt += 1
    if n < 0:
        cnt = -1
        break

if cnt == -1:
    print("-1")
else:
    cnt += n // 5
    print(cnt)