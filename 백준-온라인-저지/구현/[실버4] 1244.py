# https://www.acmicpc.net/problem/1244

import sys
input = sys.stdin.readline

n = int(input())
switch = list(map(int, input().split()))
stu = int(input())

def boy_switch(num):
    for i in range(n):
        if (i+1) % num == 0:
            switch[i] = (switch[i] + 1) % 2
    
def girl_switch(num):
    switch[num] = (switch[num] + 1) % 2
    left = num - 1
    right = num + 1
    while left >= 0 and right < n and switch[left] == switch[right]:
        switch[left] = (switch[left] + 1) % 2
        switch[right] = (switch[right] + 1) % 2
        left -= 1
        right += 1

for _ in range(stu):
    sex, num = map(int, input().split())
    if sex == 1:
        boy_switch(num)
    else:
        girl_switch(num-1)
    
k = 0
while switch[k:k+20]:
    result = switch[k:k+20]
    print(*result)
    k += 20
# 출력: 한 줄에 20개씩