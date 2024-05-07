import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    a = input()
    a1 = a[:1] + a[-2:]
    print(f"{a1.rstrip()}")