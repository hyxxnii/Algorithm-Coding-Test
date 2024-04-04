# https://www.acmicpc.net/problem/15652

import sys
from itertools import combinations_with_replacement

n, m = map(int, input().split())
data = list(range(1, n+1))
result = list(combinations_with_replacement(data, m))

for i in result:
    print(*i)