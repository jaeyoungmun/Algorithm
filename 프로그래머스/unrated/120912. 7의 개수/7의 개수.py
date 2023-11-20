def solution(array):
    seven = 0
    array = str(array)
    for i in range(len(array)):
        if array[i:i+1] == '7':
            seven += 1
    return seven