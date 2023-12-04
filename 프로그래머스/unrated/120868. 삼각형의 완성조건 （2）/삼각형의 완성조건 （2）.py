def solution(sides):
    # big이 가장 긴 경우 - line이 1부터 늘어가면서 sides[0] + line == big면 break
    # line이 가장 긴 경우 - line이 위 상태에서 1씩 늘어나면서 sides[0] + sides[1] == line이면 break
    # sides[0] 과 sides[1]이 동시에 가장 길 때
    sides.sort()
    sides.append(0)
    count = 0
    while(1):
        sides[2] += 1
        if sides[0] + sides[2] <= sides[1]:
            continue
        elif sides[0] + sides[2] > sides[1] and sides[1] >= sides[2]:
            # print(sides[2])
            count += 1
        elif sides[0] + sides[1] > sides[2]:
            # print(sides[2])
            count += 1
        elif sides[0] + sides[1] <= sides[2]:
            # print("break: ",sides[2])
            break
    return count