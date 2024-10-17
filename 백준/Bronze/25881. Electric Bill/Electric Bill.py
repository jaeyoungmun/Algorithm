import sys
input = sys.stdin.readline

b1, b2 = map(int, input().split())
n = int(input())

for _ in range(n):
    k = int(input())
    if k <= 1000:
        print(k, k * b1)
    else:
        print(k, b1*1000+b2*(k-1000))