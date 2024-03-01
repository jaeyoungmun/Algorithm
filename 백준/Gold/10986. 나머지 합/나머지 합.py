import sys
input = sys.stdin.readline

n,m = map(int, input().split())
S = [0] * (n+1)
D = [0] * m
sum = 0
A = list(map(int, input().split())) # 원본 리스트 생성

for i in range(1,n+1): # 합배열 생성
    S[i] = S[i-1] + A[i-1]
S.pop(0)

for i in range(n): # 합배열 모듈 연산 
    remainder = S[i] % m
    if (remainder== 0):
        sum += 1
    D[remainder] += 1

for i in range(m):
    if D[i] > 1:
        sum += (D[i] * (D[i]-1) // 2)

print(sum)