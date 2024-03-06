### 1차 풀이
# 볼링공 N개, 최대 무개 M => 두 사람이 고를 수 있는 볼링공 번호의 조합
# 같은 무게라도 서로 다른 공으로 간주

# n, m = map(int, input().split()) # 5 3
# data = list(map(int, input().split())) # 1 3 2 3 2

# count = 0
# for i in range(len(data)):
#     for j in range(i+1, len(data)):
#         if data[i] != data[j]:
#             count +=1 
            
# print(count)

### 교재 정답 풀이
# 무게마다 볼링공이 몇 개 있는지 계산 => A가 특정 무게의 공을 선택했을 때, A가 선택한 특정 무게의 공들을 제외한 나머지 공의 개수만큼 B가 선택 가능 (중복 조합 제외)

n, m = map(int, input().split()) # 5 3
data = list(map(int, input().split())) # 1 3 2 3 2

weight = [0] * (m+1)
count = 0

for x in data: # 각 무게에 해당하는 볼링공 개수 세기
    weight[x] += 1

for i in range(1, len(weight)):
    n -= weight[i] # 무게가 i인 볼링공 개수 제외 (A가 선택할 수 있는 개수)
    count += weight[i] * n # B가 선택하는 경우의 수와 곱하기

print(count)