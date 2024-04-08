# https://www.acmicpc.net/problem/21314

import sys
input = sys.stdin.readline

data = input().rstrip()
k_loc = []
m_loc = []
for i in range(len(data)):
    if data[i] == "K":
        k_loc.append(i)
    else:
        m_loc.append(i)

def cal_max(data, k_loc):
    result = ""
    start = 0
    for i in k_loc: # max
        cnt = data[start:i+1].count("M")
        result += str(5 * 10**cnt)
        start = i + 1
    
    if start <= len(data) - 1:
        cnt = data[start:].count("M")
        result += "1" * cnt
    
    return result

def cal_min(data):
    result = ""
    start = 0
    for i in k_loc: # max
        cnt = data[start:i+1].count("M")
        if cnt >= 1:
            result += str(10**(cnt-1))
        result += "5"
        start = i + 1
    
    if start <= len(data) - 1:
        cnt = data[start:].count("M")
        result += str(10**(cnt - 1))
    
    return result

if len(k_loc) == 0: # M으로만 이루어진 문자열
    cnt = data.count("M")
    max_ = "1" * cnt
    min_ = 10**(cnt-1)
    print(max_)
    print(min_)
    
else:
    print(int(cal_max(data, k_loc)))
    print(int(cal_min(data)))