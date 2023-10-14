def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
        elif i == 0:
            answer.append(arr[i])
    return answer