def solution(my_string):
    new = ""
    for i in range(1,len(my_string)+1):
        new += my_string[-i]
    return new
