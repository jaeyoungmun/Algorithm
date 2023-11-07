def solution(numbers):
    L = []
    temp = 0
    for i in range(len(numbers)):
        temp = numbers[i] * 2
        L.append(temp)
    return L