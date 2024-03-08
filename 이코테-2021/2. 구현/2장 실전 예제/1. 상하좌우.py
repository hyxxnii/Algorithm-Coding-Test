n = int(input())
move = input().split()
data = {
    "L": -1,
    "R": 1,
    "U": -1,
    "D": 1
}

start = 1
end = 1

for m in move:
    if m in ["L", "R"]:
        tmp = end + data[m]
        if tmp <= 0 or tmp > n:
            continue
        end = tmp
    else:
        tmp = start + data[m]
        if tmp <= 0 or tmp > n:
            continue
        start = tmp
    
print(start, end)

#####################
# 교재 풀이법
#####################

n = int(input()) # 5
plans = input().split() # R R R U D D
x, y = 1, 1
moves = ['L', 'R', 'U', 'D']

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for p in plans:
    for i, m in enumerate(moves):
        if p == m:
            nx = x + dx[i]
            ny = y + dy[i]
            break
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x = nx
    y = ny
    
print(x, y)