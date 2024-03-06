### 1차 풀이
# 0~9의 숫자로 이루어진 문자열 => 왼쪽부터 순차적으로 숫자 사이에 'x' 혹은 '+' 연산자 이용하여 최대값 만들기
string = input()

result = 0

for s in string: # 29810
    if s in "01":
        result += int(s)
    elif result == 0:
        result += int(s)
    else:
        result *= int(s)

print(result)


### 교재 정답 풀이
string = input()

result = int(string[0])

for i in range(1, len(string)):
    # 두 수 중에서 하나라도 '0' 또는 '1' => 더하기 수행
    num = int(string[i])
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num
print(result)