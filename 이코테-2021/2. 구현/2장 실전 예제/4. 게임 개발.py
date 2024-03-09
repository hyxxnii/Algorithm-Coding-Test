n, m = map(int, input().split())
a, b, d = map(int, input().split())
# d: 0=북쪽, 1=동쪽, 2=남쪽, 3=서쪽
# 반시계방향 => +1 
# 0: 육지 / 1: 바다

maps = [list(map(int, input().split())) for _ in range(n)]
print(maps)
check = [[0] * m for _ in range(n)] # 방문 여부
check[a][b] = 1
steps = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북, 동, 남, 서

cnt = 1
flag = 0
while True:
    # print("현재 위치: ", a, b, "cnt: ", cnt)
    # if a == b == 2:
    #     break
    
    # if flag == -1:
    #     break
    
    d = (d + 3) % 4 # 왼쪽 방향 회전 수행
    nx = a + steps[d][0]
    ny = b + steps[d][1]
    
    if flag >= 4: # 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 경우
        # 방향 유지한 채로 한 칸 뒤로
        # nx = nx + (-1 * steps[d][0])
        # ny = ny + (-1 * steps[d][1])
        nx = a + (-1 * steps[d][0])
        ny = b + (-1 * steps[d][1])
        
        if maps[nx][ny] == 1: # 이때 뒤쪽 방향이 바다이면 종료
            break
        
    if (nx < 0 or ny < 0) or (maps[nx][ny] == 1) or (check[nx][ny] == 1):
        flag += 1
        continue
    
    # 회전한 방향에서 한칸 전진
    check[nx][ny] = 1
    a = nx
    b = ny
    flag = 0
    cnt += 1

print(cnt)

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1