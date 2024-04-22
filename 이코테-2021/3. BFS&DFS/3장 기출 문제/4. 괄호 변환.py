def is_correct(p):
    cnt = 0
    for i in p:
        if i == '(': 
            cnt += 1
        else:
            if cnt == 0: 
                return False
            else: 
                cnt -= 1
    return True

def seperate_to_balance(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(': cnt +=1
        else: cnt -= 1
        if cnt == 0:
            break
    return i
    
def solution(p):
    if is_correct(p):
        return p
    
    inx = seperate_to_balance(p)
    u = p[:inx+1]
    v = p[inx+1:]
    if is_correct(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
        
    return answer