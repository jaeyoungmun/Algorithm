def solution(num_list, n):
    answer = []
    num = len(num_list)//n
    print(num)
    for i in range(num):
        temp = num_list[i*n:(i+1)*n]
        answer.append(temp)
    return answer