
n = int(input())
for i in range(n):
    for j in range(i):
        print(' ',end='')
    for k in range(2*n-(i*2+1)):
        print('*',end='')
    print()