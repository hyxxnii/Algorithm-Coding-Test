#############################################
# 풀이 방법 1
############################################# 
import sys
input = sys.stdin.readline

N, x = map(int, input().split())
data = list(map(int, input().split()))

from bisect import bisect_left
def count_num(data, x):
    return bisect_left(data, x)

idx = count_num(data, x)
cnt = 0
while idx < N:
    if data[idx] == x:
        cnt += 1
    idx += 1
    
if cnt > 0:
    print(cnt)
else:
    print("-1")
    
    
#############################################
# 풀이 방법 2
#############################################
import sys
input = sys.stdin.readline

N, x = map(int, input().split())
data = list(map(int, input().split()))

def search_start(start, end, data, x):
    if start > end:
        return None
    
    mid = (start + end) // 2
    # print(mid)
    if data[mid] == x:
        if mid == 0 or data[mid - 1] < x:
            return mid
    if data[mid] >= x:
        return search_start(start, mid - 1, data, x)
    elif data[mid] < x:
        return search_start(mid + 1, end, data, x)

def search_end(start, end, data, x):
    if start > end:
        return None

    mid = (start + end) // 2
    # print(mid)
    if data[mid] == x:
        if mid == N-1 or data[mid + 1] > x:
            return mid
    if data[mid] <= x:
        return search_end(mid + 1, end, data, x)
    elif data[mid] > x:
        return search_end(start, mid - 1, data, x)

s = search_start(0, N-1, data, x)
e = search_end(0, N-1, data, x)

if s and e:
    print(e - s + 1)
else:
    print("-1")