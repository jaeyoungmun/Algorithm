def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        if (my_string[i:i+1] not in answer):
            answer += my_string[i:i+1]
    return answer