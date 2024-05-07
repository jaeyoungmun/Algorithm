import sys
input = sys.stdin.readline
max = 0
for i in range(9):
    a = int(input())
    if max < a:
        max = a
        answer = i+1
print(f"{max}\n{answer}")