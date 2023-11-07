def solution(numer1, denom1, numer2, denom2):
    numer3 = numer1 * denom2 + denom1 * numer2
    denom3 = denom1 * denom2
    a = numer3
    b = denom3
    while b > 0:
        a, b = b, a%b
    gcd = a
    answer = [numer3/gcd, denom3/gcd]
    return answer
