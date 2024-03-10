# https://www.acmicpc.net/problem/20546

money = int(input())
stocks = list(map(int, input().split()))

def cal_j():
    left_money = money
    stock_n = 0
    
    for s in stocks:
        stock_n += left_money // s
        left_money = left_money % s
        if left_money == 0:
            break
        
    return left_money, stock_n
        
def cal_s():
    left_money = money
    stock_n = 0
    
    for i in range(len(stocks)-4):
        if stocks[i] < stocks[i+1] < stocks[i+2] < stocks[i+3]: # 3일 연속 상승
            left_money += stocks[i+3] * stock_n # 전량 매도
            stock_n = 0
        
        if stocks[i] > stocks[i+1] > stocks[i+2] > stocks[i+3]: # 3일 연속 하락
            stock_n += left_money // stocks[i+3] # 전량 매수
            left_money = left_money % stocks[i+3]

    return left_money, stock_n

money_j, stock_j = cal_j()
money_s, stock_s = cal_s()
result_j = money_j + stock_j * stocks[-1]
result_s = money_s + stock_s * stocks[-1]

if result_j > result_s:
    print("BNP")
elif result_j < result_s:
    print("TIMING")
else:
    print("SAMESAME")