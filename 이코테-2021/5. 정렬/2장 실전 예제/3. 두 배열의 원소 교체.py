import sys
input = sys.stdin.readline

# A 배열 모든 원소 합이 최대가 되도록 => B에서 가장 큰 것과 A에서 가장 작은 걸 바꿔치기
n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else: # A의 각 원소가 B의 모든 원소보다 클 수도 있기에, 그러면 굳이 반복문 안 돌아도 됨
        break

print(sum(A))