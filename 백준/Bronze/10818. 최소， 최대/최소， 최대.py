import sys
input = sys.stdin.readline

n = int(input())
a = (input().split())
max = int(a[0])
min = int(a[0])
for i in range(n):
    a[i] = int(a[i])
    if max < a[i]:
        max = a[i]
    elif min > a[i]:
        min = a[i]
print(f"{min} {max}")