loc = input()
cnt = 0

x_dict = {
    "a":1,
    "b":2,  
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
}

x = x_dict[loc[0]] # 1
y = int(loc[1]) # 1

move_x = [-2, -2, 2, 2, -1, -1, 1, 1]
move_y = [-1, 1, -1, 1, -2, 2, -2, 2]

# 첫번째 경우
for i, (mx, my) in enumerate(zip(move_x, move_y)):
    nx = x + mx
    ny = y + my
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue

    cnt += 1

print(cnt)

#####################
# 교재 풀이법
#####################

loc = input()
row = int(loc[1])
col = int(ord(loc[0]) - int(ord('a'))) + 1

# 나이트가 이동할 수 있는 8가지 방향
steps = [(-2, 1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

cnt = 0
for i, step in enumerate(steps):
    nx = row + step[0]
    ny = col + step[1]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue

    cnt += 1

print(cnt)