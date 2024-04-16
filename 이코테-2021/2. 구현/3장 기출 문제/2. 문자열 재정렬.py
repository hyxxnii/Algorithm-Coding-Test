import sys
input = sys.stdin.readline

S = input().rstrip()
string = ""
num = ""
for i in S:
    if i.isdigit():
        num += i
    else:
        string += i

print(''.join(sorted(string)) + str(sum(list(map(int, num)))))