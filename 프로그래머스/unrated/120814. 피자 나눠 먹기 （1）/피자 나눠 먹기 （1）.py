def solution(n):
    # 7 * i // n <- 이게 1이상이 되면 그거로 리턴
    for i in range(0,20):
        num = (i * 7 // n)
        if num >= 1:
            return i