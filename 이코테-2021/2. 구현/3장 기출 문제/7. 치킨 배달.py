from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 집, 치킨집 기록
house = [] # house = [(1,3), (2,5), (3,2), (4,3)]
chicken = [] # chicken = [(2,3), (3,3), (5,5)]
for i in range(n):
    data = list(map(int, input().split())) # 전체 집 정보는 저장해둘 필요 X
    for j in range(n):
        if data[j] == 1:
            house.append((i, j))
        elif data[j] == 2:
            chicken.append((i, j))

# M개의 치킨집 조합을 구해 각 집에서 해당 치킨집까지의 거리 합 구함 => 최솟값 갱신
def cal_dist(combi):
    result_dist = 0
    for xh, yh in house:
        tmp = 1e9
        for xc, yc in combi:
            tmp = min(tmp, abs(xh-xc) + abs(yh-yc))
        result_dist += tmp
    return result_dist

chicken_combi = list(combinations(chicken, m))
result = 1e9
for combi in chicken_combi:
    result = min(result, cal_dist(combi))
    
print(result)