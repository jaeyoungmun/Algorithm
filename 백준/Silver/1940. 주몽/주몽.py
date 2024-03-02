n = int(input())
m = int(input())

A = [0] * n
A = list(map(int,input().split()))
A.sort()

answer = 0
start = 0
end = -1

while(A[start] != A[end]):
    if (A[start] + A[end] == m):
        answer += 1
        start += 1
    elif (A[start] + A[end] < m):
        start += 1
    elif (A[start] + A[end] > m):
        end += -1

print(answer)