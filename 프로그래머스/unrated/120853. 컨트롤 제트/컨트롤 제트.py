def solution(s):
    sum = 0
    lst = []
    lst = s.split()
    print(lst)
    for i in range(len(lst)):
        if lst[i] != 'Z':
            lst[i] = int(lst[i])
            sum += lst[i]
        elif lst[i] == 'Z':
            sum -= lst[i-1]
    return sum