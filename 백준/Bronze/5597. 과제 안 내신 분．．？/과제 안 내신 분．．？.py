import sys
input = sys.stdin.readline

a = [int(input()) for _ in range(28)]
for i in range(1,31):
    if i not in a:
        print(f"{i}")
