# https://www.acmicpc.net/problem/12933

import sys
input = sys.stdin.readline

sound = list(input().rstrip())
ans = 0

if sound[0] != "q" or sound[-1] != "k":
    print("-1")
    exit()

def find_duck(i): # i: q의 위치
    global ans
    duck = "quack"
    d = 0
    new_duck = True
    
    for i in range(len(sound)):
        if sound[i] == duck[d]:
            if sound[i] == "k": # 오리 1마리의 형태 찾았을 때 => 기존 오리인지 새로운 오리인지
                if new_duck:
                    ans += 1
                    new_duck = False
                sound[i] = 0
                d = 0 # 다시 q 위치로 => 다시 k까지 도달해서 오리 형태를 접했을 때 이제는 기존 오리로 판단 (카운트 x)
                continue # d = 0으로 유지한 채 다시 q부터 찾으러
            sound[i] = 0
            d += 1

for i in range(len(sound) - 4):
    if sound[i] == 'q': # q를 만나면 그 뒤에 uack를 찾으러
        find_duck(i)

if ans == 0 or any(sound):
    print("-1")
else:
    print(ans)