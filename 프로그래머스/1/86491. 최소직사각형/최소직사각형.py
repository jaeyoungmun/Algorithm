def solution(sizes):
    max_w = 0
    max_h = 0
    for i in range(len(sizes)):
        sizes[i].sort()
    for i in range(len(sizes)):
        if sizes[i][0] > max_w:
            max_w = sizes[i][0]
        if sizes[i][1] > max_h:
            max_h = sizes[i][1]
    return max_h * max_w