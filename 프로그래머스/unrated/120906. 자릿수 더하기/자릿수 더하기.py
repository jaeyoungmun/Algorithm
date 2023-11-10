def solution(n):
    answer = 0
    for i in range(len(str(n))+1):
        answer += n % 10
        n = n//10
        # print(answer)
    return answer