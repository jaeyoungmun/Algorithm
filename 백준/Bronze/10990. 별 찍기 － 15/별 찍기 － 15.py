n = int(input())
# for i in range(n):
#     for j in range(n-i-1,0,-1):
#         print(' ',end=' ')
#     print('*',end=' ')
#     for k in range(2*i-1):
#         print(' ',end=' ')
#     if (i != 1):
#         print('*',end=' ')
#     print( )
#     왜 이거는 출력 형식이 잘못되었습니다 라고 하는가...
for i in range(n):
    print(' ' * (n-i-1) + '*',end='')
    if i>0:
        print(' ' * (2*i-1) + '*',end='')
    print()