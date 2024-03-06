### 1차 & 교재 풀이
# 0과 1로 이루어진 문자열 => 모든 숫자를 같게 만들 때 '연속된 하나 이상의 숫자를 잡고 모두 뒤집기'
# 뒤집는 행동의 최소 횟수 구하기

string = input()
count_0 = 0 # 0으로 뒤집는 횟수
count_1 = 0 # 1로 뒤집는 횟수

if string[0] == '0':
    count_1 += 1
else:
    count_0 += 1

for i in range(len(string) - 1):
    if string[i] != string[i+1]:
        if string[i+1] == '0':
            count_1 += 1
        else:
            count_0 += 1
    
print(min(count_0, count_1))