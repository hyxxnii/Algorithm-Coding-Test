### 1차 풀이
# n = int(input()) # 5
# scary = list(map(int, input().split())) # 2, 3, 1, 2, 2

# scary.sort() # 오름차순
# # 1 2 2 2 3

# idx = -1
# result = 0

# while True:
#     idx = idx - scary[idx] 
#     result += 1
#     if idx < -n:
#         break

# print(result)


### 교재 정답 풀이 1
# 오름차순 정렬 -> 항상 최소한의 모험가 수만 포함하여 최대한 많은 그룹을 구성하게끔
# '현재 그룹에 포함된 모험가의 수'가 '현재 확인하고 있는 공포도'보다 크거나 같다면 그룹으로 설정
n = int(input()) # 5
scary = list(map(int, input().split())) # 2, 3, 1, 2, 2

scary.sort()
result = 0 # 총 그룹 수
member = 1

for m in scary:
    if member >= m:
        result += 1
        member = 1
    else:
        member += 1
        
print(result)
