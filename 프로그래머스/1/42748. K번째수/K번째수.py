def solution(array, commands):
#     commands[i] i <= 50
#     commands[i][0]-1 <= i
#     commands[i][1] <= j
#     commands[i][2] <= k
#     answer = array[i,j]
#     answer.sort
#     answer[k]
#     result.append(answer[k])
    answer = []
    for n in range(len(commands)):
        i = commands[n][0] - 1
        j = commands[n][1]
        k = commands[n][2] - 1
        temp = array[i:j]
        temp.sort()
        answer.append(temp[k])
    return answer
