################################################################
# 1. 백트래킹
################################################################
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split())) # +, -, x, //

minimum = 1e9
maximum = -1e9

def dfs(i, res, plus, sub, mul, div):
    global minimum, maximum
    
    if i == n:
        minimum = min(minimum, res)
        maximum = max(maximum, res)
        return

    if plus:
        dfs(i+1, res+nums[i], plus-1, sub, mul, div)
    if sub:
        dfs(i+1, res-nums[i], plus, sub-1, mul, div)
    if mul:
        dfs(i+1, res*nums[i], plus, sub, mul-1, div)
    if div:
        dfs(i+1, int(res/nums[i]), plus, sub, mul, div-1)
    

dfs(1, nums[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)



################################################################
# 2. 순열
################################################################
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
operation = list(map(int, input().split())) # +, -, x, //
op_list = []
for i in range(4):
    if i == 0:
        op_list.extend(['+'] * operation[i])
    elif i == 1:
        op_list.extend(['-'] * operation[i])
    elif i == 2:
        op_list.extend(['x'] * operation[i])
    else:
        op_list.extend(['/'] * operation[i])

op_product = list(permutations(op_list))

minimum = 1e9
maximum = -1e9
for op in op_product:
    res = nums[0]
    # 모든 조합에 대해 수행
    for i in range(len(op)):
        if op[i] == '+':
            res += nums[i+1]
        elif op[i] == '-':
            res -= nums[i+1]
        elif op[i] == 'x':
            res *= nums[i+1]
        else:
            res = int(res/nums[i+1])
            
    # 최소/최대값 업데이트
    minimum = min(minimum, res)
    maximum = max(maximum, res)

print(maximum)
print(minimum)