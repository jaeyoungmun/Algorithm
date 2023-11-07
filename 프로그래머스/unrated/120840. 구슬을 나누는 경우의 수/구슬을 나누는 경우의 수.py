def fac(n):
    if n > 1:
        return n * fac(n-1)
    return 1

def solution(balls, share):
    # print(fac(balls)/((fac(balls-share))*fac(share)))
    answer = fac(balls) / ((fac(balls-share))*(fac(share)))
    return answer