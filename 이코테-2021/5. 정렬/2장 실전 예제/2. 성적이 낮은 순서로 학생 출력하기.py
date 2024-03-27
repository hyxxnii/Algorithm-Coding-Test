import sys
input = sys.stdin.readline
n = int(input())
grade = []

for _ in range(n):
    info = input().split()
    grade.append((info[0], int(info[1])))

grade = sorted(grade, key=lambda x: x[1])
for i in grade:
    print(i[0], end=' ')
