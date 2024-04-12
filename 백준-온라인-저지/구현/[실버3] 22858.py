# https://www.acmicpc.net/problem/22858
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# R_card = list(map(int, input().split()))
# D_card = list(map(int, input().split()))
P_card = [[0] * n for _ in range(k+1)]
P_card[0] = list(map(int, input().split()))
D_card = list(map(int, input().split()))

for i in range(1, k+1):
    for j in range(n):
        P_card[i][D_card[j] - 1] = P_card[i-1][j]


print(*P_card[-1])