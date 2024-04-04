# https://www.acmicpc.net/problem/1969
import sys
from scipy.spatial import distance
input = sys.stdin.readline

n, m = map(int, input().split())
dna = list([input().rstrip() for _ in range(n)])
candi = ['A', 'C', 'G', 'T'] # 사전순 (max했을 때 가장 앞선 순으로 처리하기위해)

result = ''
hamming_dist = 0
for i in range(m): # 각 dna에 대한 i번째 글자
    cnt_list = [0] * 4 # A, C, G, T
    for j in range(n):
        if dna[j][i] == 'A':
            cnt_list[0] += 1
        elif dna[j][i] == 'C':
            cnt_list[1] += 1
        elif dna[j][i] == 'G':
            cnt_list[2] += 1
        else:
            cnt_list[3] += 1
    
    max_dna = cnt_list.index(max(cnt_list))
    result += candi[max_dna]
    
    for j in range(n):
        if dna[j][i] != candi[max_dna]:
            hamming_dist += 1
            
print(result)
print(hamming_dist)