def solution(progresses, speeds):
    # progresses[i] += speeds[i]
    # i번째가 100 달성 => i++ => i번째가 100넘는지 확인 if O => i++
    i = 0 #작업물의 순서
    day = 0 #작업일
    temp = []
    answer = []
    while(i < len(progresses)):
        # print(i)
        if progresses[i] + (speeds[i] * day) > 99:
            temp.append(i)
            i += 1
        else:
            if len(temp) > 0:
                answer.append(len(temp))
                temp = []
            day += 1
    answer.append(len(temp))
    return answer