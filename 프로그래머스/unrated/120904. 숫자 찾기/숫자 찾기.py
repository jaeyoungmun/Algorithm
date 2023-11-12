def solution(num, k):
    num = str(num)
    index = num.find(str(k))
    if index == -1:
        return index
    return index + 1