import sys
input = sys.stdin.readline

n = int(input())
lst =[]

for i in range(n):
    p = input()
    if not lst or p != lst[-1]:
        lst.append(p)

print(len(lst)+1)