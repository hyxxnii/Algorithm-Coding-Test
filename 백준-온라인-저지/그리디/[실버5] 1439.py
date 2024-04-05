# https://www.acmicpc.net/problem/1439

import sys
input = sys.stdin.readline

S = input().rstrip()
data = [0, 0] # 0과 1의 연속된 숫자 집합 개수

i = 0
while i <= len(S) - 1:
    start = S[i]
    while True:
        if i >= len(S) or start != S[i]:
            break
        i += 1
    data[int(start)] += 1

if 0 in data:
    print("0")
else:
    print(min(data))
    
###############################
# 더 간결한 코드
################################
s=input()
cnt=0
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        cnt+=1
print((cnt+1)//2)