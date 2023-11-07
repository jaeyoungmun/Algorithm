def solution(my_string, letter):
    while(letter in my_string):
        index = my_string.find(letter)
        my_string = my_string[:index] + my_string[index+1:]
    return my_string
