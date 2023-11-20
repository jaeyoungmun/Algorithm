def solution(my_str, n):
    answer = []
    i = 0
    while(1):
        answer.append((my_str[i:i+n]))
        i += n
        if i >= len(my_str):
            break
    return answer