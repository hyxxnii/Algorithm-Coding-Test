# https://www.acmicpc.net/problem/19939

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
basket = [0] * (k+1)
min_sum = (k * (k+1)) / 2

if min_sum > n:
    print("-1")
elif min_sum == n:
    print(k - 1)
else:
    basket = [i for i in range(k+1)]
    remain = n - min_sum
    i = k
    while remain != 0:
        basket[i] += 1
        i -= 1
        remain -= 1
        if i == 0:
            i = k
    print(basket[k] - basket[1])