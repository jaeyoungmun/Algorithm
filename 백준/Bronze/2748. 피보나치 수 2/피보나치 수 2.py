import sys
input = sys.stdin.readline

lst = [0,1]

n = int(input())
for i in range(2,n+1):
    lst.append(lst[i-2] + lst[i-1])

print(lst[n])