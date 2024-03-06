### 1차 + 교재 정답 풀이
# N개의 동전 => 만들 수 없는 양의 정수 금액 중 최솟값 구하기

n = int(input()) # 5
data = list(map(int, input().split())) # 3 2 1 1 9

data.sort()
result = 1 # 비교할 양의 정수

for num in data:
    if num > result:
        break
    result += num

print(result)