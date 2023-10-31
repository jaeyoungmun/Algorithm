def solution(array):
    for i in range(1,len(array)):
        for j in range(i-1, -1, -1):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
                i -= 1
    answer = array[len(array)//2]

    return answer