import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
print(f'{min(A)} {max(A)}')