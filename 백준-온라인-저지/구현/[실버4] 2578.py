# https://www.acmicpc.net/problem/2578

import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
calls = [list(map(int, input().split())) for _ in range(5)]

def check_bingo(ans):
    global result
    global flag 
    
    for x in range(5):
        for y in range(5):
            if board[x][y] == ans:
                board[x][y] = 0

                # 가로
                if sum(board[x]) == 0:
                    result += 1
                # 세로
                sum_h = 0
                for h in range(5):
                    sum_h += board[h][y]
                if sum_h == 0:
                    result += 1
                
                # 대각선 1
                sum_h = 0
                if x + y == 4:
                    for h in range(5):
                        sum_h += board[4-h][h]
                    if sum_h == 0:
                        result += 1

                # 대각선 2
                sum_h = 0
                if x - y == 0:
                    for h in range(5):
                        sum_h += board[h][h]
                    if sum_h == 0:
                        result += 1
                break
        
    if result >= 3:
        flag = 1
    # return bingo

result = 0
num = 0
flag = 0
for i in range(5):
    for j in range(5):
        num += 1
        check_bingo(calls[i][j])

        if result >= 3:
            break
    if flag == 1:
        print(num)
        break