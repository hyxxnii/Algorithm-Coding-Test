N, M, K = map(int, input().split()) # 5 8 3
num_list = list(map(int, input().split())) # 2 4 5 4 6

# 정렬
num_list.sort() # [2, 4, 4, 5, 6]
max_1 = num_list[-1]
max_2 = num_list[-2]
print(num_list)

result = 0
cnt = 0
for i in range(M):
    if cnt == K:
        result += max_2
        cnt = 0
    else:
        result += max_1
        cnt += 1
    
print(result)


#####################
# 교재 풀이법

n, m, k = map(int, input().split()) # 5 8 3
num_list = list(map(int, input().split())) # 2 4 5 4 6

# 정렬
num_list.sort() # [2, 4, 4, 5, 6]
first = num_list[n-1]
second = num_list[n-2]

result = 0

while True:
    for i in range(k): # 가장 큰 수 k번 더하기
        result += first
        m -= 1
        if m == 0: 
            break
    
    result += second # 두 번째로 큰 수 한 번 더하기
    m -= 1
    if m == 0:
        break
    
print(result)


# 교재 풀이 2: 간단한 코드 풀이
N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True) # 내림차순 정렬
# 6 5 4 4 2
first = nums[0]
second = nums[1]

answer = 0
count = int(M / (K+1)) * K + (M % (K+1))
answer += count * first
answer += (M - count) * second
print(answer)

