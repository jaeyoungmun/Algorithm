def solution(my_string):
    # print(my_string[6])
#     포문에서 숫자찾으면 알파벳나오기전까지 찾고 슬라이싱
#     
#     숫자위치 start_idx / end_idx 
#     num변수에 형변환해서 저장
#     
    number = "0123456789"
    start_idx = -1
    sum1 = 0
    for i in range(len(my_string)):
        if my_string[i] in number: #숫자일때
            if start_idx == -1: #처음 숫자일때
                start_idx = i
        elif my_string[i] not in number: #숫자가 아닐때
            if start_idx != -1: #연속된 숫자
                # print(i)
                end_idx = i
                sum1 += int(my_string[start_idx:end_idx])
                start_idx = -1
#                 숫자로 끝나는 문자에선 마지막 숫자가 합산이 안됨
#                 길이가 1인 숫자있는 문자열도 안됨
    if start_idx != -1: #초기화가 안됨 -> 숫자로 끝남
        sum1 += int(my_string[start_idx:])
    answer = 0
    return sum1

