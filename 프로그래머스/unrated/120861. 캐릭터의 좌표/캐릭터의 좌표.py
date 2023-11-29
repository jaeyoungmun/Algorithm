def solution(keyinput, board):
    # print(9//2) #4
    limit_row = board[0]//2
    limit_column = board[1]//2
    answer = [0,0]
    for i in range(len(keyinput)):
        if keyinput[i] == "left":
            answer[0] -= 1
        elif keyinput[i] == "right":
            answer[0] += 1
        elif keyinput[i] == "up":
            answer[1] += 1
        elif keyinput[i] == "down":
            answer[1] -= 1
        
        if answer[0] > limit_row:
            answer[0] = limit_row
        elif answer[0] < -(limit_row):
            answer[0] = -(limit_row)
        if answer[1] > limit_column:
            answer[1] = limit_column
        elif answer[1] < -(limit_column):
            answer[1] = -(limit_column)
    # print("limit_column",limit_column)
    return answer