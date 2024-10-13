T = int(input())

for _ in range(T):
    a = int(input())
    b = int(input())
    lst = [[0] * b for _ in range((a+1))]
    # print(lst)
    for j in range(b):
        lst[0][j] = j+1
    # print(lst)
    
    for k in range(1,a+1):
        for n in range(b):
            lst[k][n] = lst[k-1][n] + lst[k][n-1]
    print(lst[a][b-1])