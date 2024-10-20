import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    b = [1] * n
    for i in range(n):
        if i > 0 and b[i-1] >= b[i]:
            b[i] = b[i-1] + 1
        if a[i] == b[i]:
            b[i] += 1
    print(b[n-1])
