import sys
input = sys.stdin.readline

A = input()
low = A.lower()
up = A.upper()
A = list(A)
low = list(low)
up = list(up)
for i in range(len(A)):
    if A[i] == low[i]:
        A[i] = A[i].upper()
    elif(A[i] == up[i]):
        A[i] = A[i].lower()
for i in A:
    print(i, end="")