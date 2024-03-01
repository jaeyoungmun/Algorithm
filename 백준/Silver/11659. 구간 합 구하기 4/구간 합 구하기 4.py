import sys
input = sys.stdin.readline

n, m = map(int, input().split())
S = [0] * (n+1)

A = list(map(int, input().split()))

for i in range(1,n+1):
    S[i] = S[i-1] + A[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(S[j] - S[i-1])