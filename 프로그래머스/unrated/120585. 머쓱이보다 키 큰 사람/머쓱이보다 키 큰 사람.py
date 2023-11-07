def solution(array, height):
    array.sort()
    count = 0
    print(array)
    for i in array:
        if height < i:
            count +=1
    return count