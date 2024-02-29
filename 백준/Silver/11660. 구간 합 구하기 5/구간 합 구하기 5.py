import sys
input = sys.stdin.readline

n,m = map(int, input().split())
A = [[0] * n for _ in range(n)]
D = [[0] * (n+1) for _ in range(n+1)]
# print(n)
# print(A)
for i in range(n): # 원본 리스트 저장
    A[i] = list(map(int, input().split()))
    # print(A)

for i in range(1,n+1): # 합배열 미리 생성
    for j in range(1,n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i-1][j-1]

for _ in range(m): # 요구사항 m번 실행
    x1, y1, x2, y2 = map(int, input().split())
    print(D[x2][y2] + D[x1 -1][y1 -1] - D[x2][y1-1] - D[x1-1][y2])