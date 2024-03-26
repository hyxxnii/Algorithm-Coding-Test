import sys

input = sys.stdin.readline
x = int(input())

d = [0] * 30001 # d[1]은 최종적으로 1에 도달한 것이므로 카운트 0으로 둠 (이미 도달했으니 연산할 카운트가 없는거지)
for i in range(2, x+1): # Bottom-up
    # 1을 뺀 경우
    d[i] = d[i-1] + 1
    # 2로 나누는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    # 3으로 나누는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    # 5로 나누는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
        
print(d[x])