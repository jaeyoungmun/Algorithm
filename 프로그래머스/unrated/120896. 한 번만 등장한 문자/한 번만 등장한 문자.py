def solution(s):
    answer = ''
    result = ''
    for i in s:
        if s.count(i) == 1:
            answer += i
    for i in range(len(answer)):
        temp = min(answer)
        result += temp
        answer = answer.replace(temp,'~')
        print(temp)
    return result
    # print(min(answer))
    
        
    # if 'a' < 'b':
    #     print('a')
    # return answer.sort()