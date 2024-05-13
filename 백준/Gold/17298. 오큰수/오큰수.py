import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
mystack = []
answer = [0] * n

for i in range(n):
    while mystack and A[mystack[-1]] < A[i]:
        answer[mystack.pop()] = A[i]
    mystack.append(i)

while mystack:
    answer[mystack.pop()] = -1

for i in range(n):
    print(answer[i],end=' ')
