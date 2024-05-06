import sys
input = sys.stdin.readline
sum = 0
n = input()
A = list(map(int,input().split()))
v = int(input())
for i in A:
    if (i == v):
        sum += 1
print(sum)