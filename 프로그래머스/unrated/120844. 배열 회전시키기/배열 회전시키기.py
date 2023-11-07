def solution(numbers, direction):
    if direction == "right":
        temp = numbers[-1]
        for i in range(1,len(numbers)):
            numbers[-i] = numbers[-i-1]
        numbers[0] = temp
    if direction == "left":
        temp = numbers[0]
        for i in range(0,len(numbers)-1):
            numbers[i] = numbers[i+1]
        numbers[-1] = temp
    return numbers
    