import sys
input = sys.stdin.readline

# 크루스칼 알고리즘 -> 최소 신장 트리

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)
houses = []
result = 0

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    houses.append((c, a, b))

houses.sort()
max_edge = 0

for house in houses:
    c, a, b = house
    # 사이클 발생시키지 않을 때만(루트 노드가 다름) => 집합을 합침(union)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c
        max_edge = c

print(result - max_edge)