# https://www.acmicpc.net/problem/15650

import sys
from itertools import combinations


n, m = map(int, input().split())
data = list(range(1, n+1))
result = list(combinations(data, m))

for i in result:
    print(*i)