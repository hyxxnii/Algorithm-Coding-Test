# # https://www.acmicpc.net/problem/2217

# n = int(input())
# data = []
# res = [0]

# for _ in range(n):
#     data.append(int(input()))

# data = sorted(data, reverse=True)
# for x in data:
#     res.append(x * len(res))

# print(max(res))

## 더 간결한 코드
n  = int(input())
data = [int(input()) for _ in range(n)]
data.sort(reverse=True)
print(max(data[i] * (i + 1) for i in range(n)))