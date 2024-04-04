# https://www.acmicpc.net/problem/14888

#import sys
# from itertools import permutations

# input = sys.stdin.readline
# n = int(input())
# data = list(map(int, input().split()))
# op_list = list(map(int, input().split())) #  +, -, x, / 개수
# op = []
# for i in range(len(op_list)):
#     for _ in range(op_list[i]):
#         op.append(i)

# min_ = 1e9
# max_ = -1e9

# def solve():
#     global min_, max_
#     for combi in list(permutations(op, n-1)):
#         total = data[0]
#         for num in range(1, n):
#             if combi[num - 1] == 0:
#                 total += data[num]
#             elif combi[num - 1] == 1:
#                 total -= data[num]
#             elif combi[num - 1] == 2:
#                 total *= data[num]
#             elif combi[num - 1] == 3:
#                 if total < 0:
#                     total = -(-total // data[num])
#                 else:
#                     total = total // data[num]
#         if total > max_:
#             max_ = total
#         if total < min_:
#             min_ = total
# solve()
# print(max_)
# print(min_)

#####################################
# 백트랙킹 (DFS)
#####################################
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
op_list = list(map(int, input().split())) #  +, -, x, / 개수

min_ = 1e9
max_ = -1e9

def dfs(i, total, plus, minus, multiply, divide):
    global min_, max_
    if i == n:
        min_ = min(total, min_)
        max_ = max(total, max_)
        return
    
    if plus:
        dfs(i + 1, total + data[i], plus - 1, minus, multiply, divide)
    if minus:
        dfs(i + 1, total - data[i], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(i + 1, total * data[i], plus, minus, multiply - 1, divide)
    if divide:
        dfs(i + 1, int(total / data[i]), plus, minus, multiply, divide - 1)
        
dfs(1, data[0], op_list[0], op_list[1], op_list[2], op_list[3])
print(max_)
print(min_)