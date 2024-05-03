n, m = map(int, input().split())
answer = n - m
if answer < 0:
    print(answer * -1)
else:
    print(answer)
