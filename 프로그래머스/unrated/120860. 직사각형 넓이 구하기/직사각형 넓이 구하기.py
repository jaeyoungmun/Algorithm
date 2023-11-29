import math

def solution(dots):
    # row : dots[i][0]
    # column : dots[i][1]
    for i in range(4): #가로길이
        row1 = dots[0][0]
        if dots[i][0] != row1:
            row2 = dots[i][0]
    for i in range(4): #세로길이
        column1 = dots[0][1]
        if dots[i][1] != column1:
            column2 = dots[i][1]
    answer = abs(row1 - row2) * abs(column1 - column2)
    # print("가로",abs(row1 - row2))
    # print("세로",abs(column1 - column2))
    return answer