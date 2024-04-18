import sys
input = sys.stdin.readline

def rotate_90_degree(mat):
    n = len(mat)
    new_mat = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            new_mat[i][j] = mat[n-j-1][i]
    return new_mat

def check_lock(lock):
    # 자물쇠 중간 부분이 모두 1인지 확인
    true_n = len(lock) // 3
    for x in range(n):
        for y in range(n):
            if not lock[n+x][n+y]:
                return False
    return True
    
def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    # 자물쇠 크기 3배 늘리기
    large_lock = [[0] * (n*3) for _ in range(n*3)]
    for i in range(n): # 자물쇠 중앙에 원래 행렬 값 입력
        for j in range(n):
            large_lock[n+i][n+j] = lock[i][j]
    
    for _ in range(4): # 90도씩 회전
        new_key = rotate_90_degree(key)
        for x in range(n*3 - m + 1): # 행
            for y in range(n*3 - m + 1): # 열
                # 자물쇠에 열쇠 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        large_lock[x+i][y+j] += new_key[i][j]
                if check_lock:
                    return True
                
                # 자물쇠에서 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        large_lock[x+i][y+j] -= new_key[i][j]
                
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))