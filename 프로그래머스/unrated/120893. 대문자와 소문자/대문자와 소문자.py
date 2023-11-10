def solution(my_string):
    temp = ''
    for i in my_string:
        if ord(i) < 97:
            temp += i.lower()
        elif ord(i) >= 65:
            temp += i.upper()
    return temp