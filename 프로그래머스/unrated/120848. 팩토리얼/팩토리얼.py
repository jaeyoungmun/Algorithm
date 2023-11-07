def fac(n):
    if n > 1:
        return n * fac(n-1)
    else:
        return 1

def solution(n):
    for i in range(1,11):
        if fac(i) > n:
            return i-1
        elif fac(i) == n:
            return i