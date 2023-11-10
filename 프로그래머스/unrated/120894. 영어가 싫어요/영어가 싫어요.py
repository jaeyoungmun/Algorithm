def solution(numbers):
    temp = ''
    num = {"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    start = 0
    for i in range(len(numbers)+1):
        end = i
        print(start,numbers[start:i])
        if numbers[start:i] in num:
            temp += num[numbers[start:i]]
            start = i
    return int(temp)