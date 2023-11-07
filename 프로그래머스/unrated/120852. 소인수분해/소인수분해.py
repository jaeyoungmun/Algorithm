def solution(n):
    answer = []
    count = 0
    for i in range(2,n+1):
        if n == 1: # 시간 단축을 위해
            break
        if n % i ==0:
            for j in range(2,i): # i가 소인수인지 확인. 1과 자기자신으로 나누지않음
                if i % j == 0:
                    count += 1 
            if count < 1: # count가 0이어야 소인수임
                answer.append(i)
            count = 0
            n /= i
    return answer