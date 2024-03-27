import sys
input = sys.stdin.readline
n = int(input())
nums = list([int(input()) for _ in range(n)])

# 1. 선택 정렬
for i in range(n):
    min_idx = i
    for j in range(i, n):
        if nums[min_idx] > nums[j]:
            min_idx = j
    nums[i], nums[min_idx] = nums[min_idx], nums[i]

print(*nums[::-1])

# 2. 삽입 정렬
for i in range(1, n):
    for j in range(i-1, 0, -1):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            break
print(*nums[::-1])

# 3. 퀵 정렬
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    
    pivot = nums[0]
    tail = nums[1:]
    
    left = [v for v in tail if v <= pivot]
    right = [v for v in tail if v > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

result = quick_sort(nums)
print(*result[::-1])

# 4. 계수 정렬
cnt = [0] * (max(nums) + 1)
result = []
for i in nums:
    cnt[i] += 1

for i in range(len(cnt)):
    if cnt[i] != 0:
        j = cnt[i]
        while j > 0:
            result.append(i)
            j -= 1
print(*result[::-1])
