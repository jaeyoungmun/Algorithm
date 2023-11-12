def solution(array):
    maximum = array[0]
    for i in range(0,len(array)):
        if array[i] > maximum:
            maximum = array[i]
            index = i
    return [maximum,index]