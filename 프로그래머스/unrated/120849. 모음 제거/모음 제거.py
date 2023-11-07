def solution(my_string):
    for i in my_string:
        if i in 'aeiou':
            num = my_string.index(i)
            # print(i)
            my_string = my_string[:num] + my_string[num+1:]
    return my_string