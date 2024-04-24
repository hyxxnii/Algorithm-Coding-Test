def is_possible_range(x, y, N):
    return True if 0 <= x < N and 0 <= y < N else False
    
def get_possible_pos(pos, N, board):
    next_pos = []
    pos = list(pos) #sorted(list(pos))
    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 1. 상하좌우 이동
    for i in range(4):
        nx1, nx2 = dx[i] + x1, dx[i] + x2
        ny1, ny2 = dy[i] + y1, dy[i] + y2
        if is_possible_range(nx1, ny1, N) and is_possible_range(nx2, ny2, N):
            if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                next_pos.append({(nx1, ny1), (nx2, ny2)})
    
    # 2. 가로로 놓여진 경우
    if x1 == x2:
        for i in [-1, 1]: # 회전: 위/아래
            nx1, nx2 = x1 + i, x2 + i
            if is_possible_range(nx1, y1, N) and is_possible_range(nx2, y2, N):
                if board[nx1][y1] == 0 and board[nx2][y2] == 0:
                    next_pos.append({(x1, y1), (nx1, y1)})
                    next_pos.append({(x2, y2), (nx2, y2)})
                    
    # 3. 세로로 놓여진 경우
    elif y1 == y2:
        for i in [-1, 1]: # 회전: 왼쪽/오른쪽
            ny1, ny2 = y1 + i, y2 + i
            if is_possible_range(x1, ny1, N) and is_possible_range(x2, ny2, N):
                if board[x1][ny2] == 0 and board[x2][ny2] == 0:
                    next_pos.append({(x1, y1), (x1, ny1)})
                    next_pos.append({(x2, y2), (x2, ny2)})
                    
    return next_pos

def solution(board):
    from collections import deque
    
    N = len(board)
    q = deque()
    pos = {(0, 0), (0, 1)} # 로봇이 있는 두 위치에 대해 순서 상관없이 방문 여부를 확인할 수 있도록 집합 자료형 {} 사용 (e.g., {(1,1),(1,2)} 와 {(1,2),(1,1)}은 같은 자료로 취급
    q.append((pos, 0)) # 현재 로봇 위치, 시간
    visited = []
    visited.append(pos)
    
    while q:
        pos, time = q.popleft()
        if (N-1, N-1) in pos:
            return time
        
        next_pos = get_possible_pos(pos, N, board)
        for np in next_pos:
            if np not in visited:
                visited.append(np)
                q.append((np, time + 1))