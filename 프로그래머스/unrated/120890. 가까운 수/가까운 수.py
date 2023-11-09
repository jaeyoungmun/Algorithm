def solution(array, n):
    array.sort()
    for i in range(len(array)):
        if n < array[i]:
            if n == array[i-1]:
                return array[i-1]
            elif (array[i] - n) == (n - array[i-1]):
                return array[i-1]
            elif (array[i] - n) > (n - array[i-1]):
                return array[i-1]
            elif (array[i] - n) < (n - array[i-1]):
                return array[i]
    return array[-1]