import sys
input = sys.stdin.readline

def solution(s):
    result = [] # 단위별 압축된 문자열의 길이 저장
    total_len = len(s)
    for i in range(total_len // 2):
        compare = s[:i+1]
        j = i + 1
        cnt = 1
        tmp = ""
        while True:
            if j >= total_len:
                break
            if compare == s[j:j+i+1]:
                cnt += 1
            else:
                if cnt > 1:
                    tmp += str(cnt) + compare
                else:
                    tmp += compare
                cnt = 1
                compare = s[j:j+i+1]
            print(tmp)
            j += i + 1
        
        tmp += str(cnt) + compare if cnt > 1 else compare
        result.append(len(tmp))
    
    answer = min(result)
    return answer
