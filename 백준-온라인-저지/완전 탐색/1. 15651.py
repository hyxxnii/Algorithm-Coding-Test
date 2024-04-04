# https://www.acmicpc.net/problem/15651

import sys
from itertools import product

n, m = map(int, input().split())

data = list(range(1, n+1))
result = list(product(data, repeat=m))
for i in result:
    print(*i)