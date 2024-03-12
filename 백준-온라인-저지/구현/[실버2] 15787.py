# https://www.acmicpc.net/problem/15787

n, m = map(int, input().split())
trains = [[0] * 20 for _ in range(n)]
check = []

for _ in range(m):
    order = list(map(int, input().split()))
    
    if order[0] == 1:
        trains[order[1]-1][order[2]-1] = 1
    elif order[0] == 2:
        trains[order[1]-1][order[2]-1] = 0
        
    elif order[0] == 3:
        if sum(trains[order[1] - 1]) != 0:
            trains[i].pop()
            while trains[i]:
                tmp.append(trains[i].pop())
            trains[i] = tmp[:1] + tmp[1::][::-1]
    
    elif order[0] == 4:
        if sum(trains[order[1] - 1]) != 0:
            while trains[i]:
                tmp.append(trains[i].pop())
            trains[i] = tmp[:-1][::-1]
        
        
    # if o in [1, 2]:
    #     i, x = order[1] - 1, order[2] - 1
    #     if (o == 1 and trains[i][x] == 0) or (o == 2 and trains[i][x] == 1) :
    #         trains[i][x] = (trains[i][x] + 1) % 2
    
    # else:
    #     i = order[1] - 1
    #     if sum(trains[i]) != 0:
    #         tmp = [0]
    #         if o == 3:
    #             trains[i].pop()
    #             while trains[i]:
    #                 tmp.append(trains[i].pop())
                
    #             trains[i] = tmp[:1] + tmp[1::][::-1]
        
    #         else:
    #             while trains[i]:
    #                 tmp.append(trains[i].pop())
                    
    #             trains[i] = tmp[:-1][::-1]

cnt = 0
for t in trains:
    if t not in check:
        check.append(t)
        cnt += 1
        
print(cnt)