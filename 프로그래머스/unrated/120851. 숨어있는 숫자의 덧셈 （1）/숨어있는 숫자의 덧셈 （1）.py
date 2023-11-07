def solution(my_string):
    answer = []
    sum = 0
    for i in my_string:
        if i in '1234567890':
            answer.append(int(i))
    for i in range(len(answer)):
        sum += answer[i]
    return sum