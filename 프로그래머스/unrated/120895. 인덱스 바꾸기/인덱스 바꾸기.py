def solution(my_string, num1, num2):
    # a= 'wodud'
    # b = 'wlsdud'
    # a,b = b,a
    # print(a)
    a = my_string[num1]
    b = my_string[num2]
    return my_string[:num1] + b + my_string[num1+1:num2] + a + my_string[num2+1:]