def solution(dot):
#     dot[0] > 0 이면 1,4사분면
    if dot[0]>0:
        if dot[1] > 0:
            return 1
        else:
            return 4
    if dot[0] < 0:
        if dot[1] > 0:
            return 2
        else: 
            return 3