import sys
input = sys.stdin.readline

N = list(map(int, input().strip()))
i = len(N) // 2
if sum(N[:i]) == sum(N[i:]):
    print("LUCKY")
else:
    print("READY")
