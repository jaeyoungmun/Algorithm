def solution(numbers, k):
    num = 0
    k -= 1
    while(k):
        numbers[num]
        num += 2
        if num == len(numbers):
            num = 0
        elif num > len(numbers):
            num = 1
        k -= 1
    return numbers[num]