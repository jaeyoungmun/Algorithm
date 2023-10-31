def solution(n):
    lst = []
    for i in range(0,n+1):
        if i % 2 != 0:
            lst.append(i)
    return lst