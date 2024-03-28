import sys
input = sys.stdin.readline

n = int(input())
# 국어, 영어, 수학
# 국어-내림차순 => 영어-오름차순 => 수학-내림차순 => 이름-증가순(대문자가 앞에 옴)
result = []
for _ in range(n):
    res = input().split()
    result.append((res[0], int(res[1]), int(res[2]), int(res[3])))

# 파이썬 sorted의 key 함수에 여러 인자 가능! 
result = sorted(result, key=lambda x: (-x[1], x[2], -x[3], x[0]))
print(result)