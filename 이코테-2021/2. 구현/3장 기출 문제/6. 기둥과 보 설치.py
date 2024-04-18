import sys
input = sys.stdin.readline

def check_building(answer):
    for ans in answer:
        x, y, a = ans
        if a == 0: # 기둥
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        
        elif a == 1: # 보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    # 삭제 및 설치를 우선 진행해보고, 그 후에 남은 구조물 모두 하나씩 확인하며 조건에 부응하는지 확인
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 0: # 삭제
            answer.remove([x, y, a])
            if not check_building(answer):
                answer.append([x, y, a])
            
        elif b == 1: # 설치
            answer.append([x, y, a])
            if not check_building(answer):
                answer.remove([x, y, a])
    
    return sorted(answer)

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))