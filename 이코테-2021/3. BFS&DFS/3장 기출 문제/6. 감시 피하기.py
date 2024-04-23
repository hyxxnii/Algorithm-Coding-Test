################################################################
# 1. DFS 활용
# 장애물을 놓을 수 있는 모든 위치를 재귀적으로 찾아, 3개의 장애물이 놓였을 때 모든 학생이 감시를 피할 수 있는지 확인
################################################################
import sys
input = sys.stdin.readline

N = int(input())
data = []
Teacher = []
for i in range(N):
    info = list(input().split())
    data.append(info)
    for j in range(N):
        if info[j] == 'T':
            Teacher.append((i, j))

def watch(x, y, direction, tmp):
    # tmp 사용
    if direction == 0: # 상
        while x >= 0:
            if tmp[x][y] == 'S': # 학생 발견
                return True
            if tmp[x][y] == 'O': # 장애물 발견
                return False
            x -= 1
    
    if direction == 1: # 하
        while x < N:
            if tmp[x][y] == 'S':
                return True
            if tmp[x][y] == 'O':
                return False
            x += 1

    if direction == 2: # 좌
        while y >= 0:
            if tmp[x][y] == 'S':
                return True
            if tmp[x][y] == 'O':
                return False
            y -= 1
    
    if direction == 3: # 우
        while y < N:
            if tmp[x][y] == 'S': 
                return True
            if tmp[x][y] == 'O':
                return False
            y += 1
            
    return False
            
def dfs(cnt):
    if cnt == 3: # 3개의 장애물이 설치되었다면, 모든 학생들이 감시를 피할 수 있는지 체크
        tmp = [data[i] for i in range(N)] # 임시 복도에서 체크
        for x, y in Teacher: # 모든 선생님의 위치를 하나씩 확인
            for i in range(4): # 각 위치에서 상하좌우 4가지 방향 확인
                if watch(x, y, i, tmp): # 한 명의 학생이라도 감지된 경우
                    return False
        return True # 모든 선생님의 위치에서 모든 학생이 감시를 피한 경우
    
    else:
        for i in range(N):
            for j in range(N):
                if data[i][j] == 'X':
                    data[i][j] = 'O'
                    cnt += 1
                    if dfs(cnt): # True면 바로 반환
                        return True
                    data[i][j] = 'X'
                    cnt -= 1
        return False

result = dfs(0)
if result:
    print("YES")
else:
    print("NO")

################################################################
# 2. 조합 활용
# 장애물을 놓을 수 있는 모든 위치에 대해 3가지 위치의 조합을 구해 각 위치에서 감시 피할 수 있는지 여부 확인
################################################################

from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
data = []
Teacher = []
possible = []
for i in range(N):
    info = list(input().split())
    data.append(info)
    for j in range(N):
        if info[j] == 'T':
            Teacher.append((i, j))
        elif info[j] == 'X':
            possible.append((i, j))

def watch(x, y, direction):
    if direction == 0: # 상
        while x >= 0:
            if data[x][y] == 'S': # 학생 발견
                return True
            if data[x][y] == 'O': # 장애물 발견
                return False
            x -= 1
    
    if direction == 1: # 하
        while x < N:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            x += 1

    if direction == 2: # 좌
        while y >= 0:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            y -= 1
    
    if direction == 3: # 우
        while y < N:
            if data[x][y] == 'S': 
                return True
            if data[x][y] == 'O':
                return False
            y += 1
            
    return False

def check():
    for x, y in Teacher:
        for i in range(4):
            if watch(x, y, i): # 학생을 발견하면
                return True
    return False

find = True
for combi in combinations(possible, 3):
    for x, y in combi:
        data[x][y] = 'O'
    
    if not check(): # 학생을 발견하면 True 반환 => 즉, 모든 선생님이 학생 발견하지 못했을 때
        find = False
        break
    
    for x, y in combi:
        data[x][y] = 'X'

if not find:
    print("YES")
else:
    print("NO")