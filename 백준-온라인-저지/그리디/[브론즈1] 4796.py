# https://www.acmicpc.net/problem/4796

i = 0
while True:
    res = 0
    # 5 8 20
    l, p, v = map(int, input(). split())
    if l + p + v == 0:
        break

    res += (v // p) * l # 10
    
    v = v % p
    if v < l:
        res += v
    else:
        res += l
            
    i += 1
    print(f"Case {i}: {res}")