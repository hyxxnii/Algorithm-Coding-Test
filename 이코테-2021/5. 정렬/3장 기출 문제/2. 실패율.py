# # import sys
# # input = sys.stdin.readline

def solution(N, stages):
    answer = []
    leng = len(stages)
    
    for i in range(1, N+1):
        cnt = stages.count(i)
    
        if leng == 0:
            fail = 0
        else:
            fail = cnt / leng
        answer.append((i, fail))
        leng -= cnt

    answer = sorted(answer, key=lambda x: -x[1])
    answer = [a[0] for a in answer]
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))