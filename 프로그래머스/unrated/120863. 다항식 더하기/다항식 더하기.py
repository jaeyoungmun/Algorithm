def solution(polynomial):
    polynomial = polynomial.split(' + ') #리스트화
    # print(polynomial)
    # a = '23x'
    # print(a[:-1])
    num1 = 0 # 1차항
    num2 = 0 # 상수항
    for i in range(len(polynomial)):
        if  polynomial[i][-1] == 'x': # 1차항
            if polynomial[i] == 'x': # 1x의 경우
                num1 += 1
            else: 
                num1 += int(polynomial[i][:-1]) # 1x이상의 경우
        else: # 0차항
            num2 += int(polynomial[i])
    ans= ""
    # num1 부터
    if num1 == 1:
        ans += "x"
    elif num1 > 1:
        ans += f'{num1}x'
    if num1 > 0 and num2 > 0:
        ans += ' + '
    if num2 > 0:
        ans += f'{num2}'
    return ans