def solution(board):
    # n*n 배열에서 확장된 n+2 * n+2 배열 생성
    board_1 = [[0] * (len(board[0]) +2) for _ in range((len(board[0]))+2)]
    # print(board_1)
    count = 0 # 안전지대의 수
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                
                board_1[i][j] += 1
                board_1[i][j+1] += 1
                board_1[i][j+2] += 1
                board_1[i+1][j] += 1
                board_1[i+1][j+1] += 1
                board_1[i+1][j+2] += 1
                board_1[i+2][j] += 1
                board_1[i+2][j+1] += 1
                board_1[i+2][j+2] += 1
    # print(board_1)
    for i in range(1,len(board)+1):
        for j in range(1,len(board)+1):
            if board_1[i][j] == 0:
                count += 1
    return count
                