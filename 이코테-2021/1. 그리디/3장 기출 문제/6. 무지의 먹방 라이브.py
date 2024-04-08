### 1차 & 교재 정답 풀이
# 회전판 N개의 음식 -> 1번부터 순서대로 번호 라벨링
# 1번 음식 섭취 시작 -> 번호가 증가하는 순으로 음식이 앞으로 옴
# 마지막 번호 음식 섭취 후 다시 1번 음식으로
# 음식당 1초 => 이후 다음 음식(섭취해야 할 가장 가까운 번호의 음식)
# K초 후 중단 => 몇 번 음식부터 섭취해야하는지 구하기

def solution(food_times, k): 
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k: 
        return -1

    # 시간이 적은 음식부터 빼야 하므로 우선순위 큐 이용
    q = []
    for i in range(len(food_times)):
        heap.heappush(q, (food_times[i], i+1)) # (총 소요 시간, 음식 번호)의 튜플 형태로 큐에 저장
        
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식 개수
    
    # sum_value + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    
    
    answer = 0
    return answer
