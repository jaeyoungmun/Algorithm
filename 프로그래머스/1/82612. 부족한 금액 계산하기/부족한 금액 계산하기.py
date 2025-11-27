def solution(price, money, count):
    answer = 0
    if (price < 1 or price > 25000):
        return "error"
    if (money < 1 or money > 1000000000):
        return "error"
    if (count < 1 or count > 2500):
        return "error"
    
    #증가하는 이용금액의 합을 구한다
    for i in range(1, count +1):
        answer += price * i
    
    # 부족한 금액 계산
    need = answer - money

    if (need <= 0):
        return 0
    else: 
        return need