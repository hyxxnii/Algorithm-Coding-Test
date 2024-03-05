n, m = map(int, input().split()) # 행, 열

result = 0
for i in range(n):
    num_list = list(map(int, input().split()))
    min_num = min(num_list)
    result = max(result, min_num)

print(result)