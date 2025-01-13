m = int(input())

ball = 1 #처음엔 공이 1번 컵에 위치
for i in range(m):
    x, y = map(int, input().split())
    # print("x와y: ",x,y)
    if x == ball:
        ball = y
    elif y == ball:
        ball = x
    # print("바뀜! ball의 위치: ",ball)
print(ball)