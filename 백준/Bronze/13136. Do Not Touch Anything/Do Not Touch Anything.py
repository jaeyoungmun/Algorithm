# 13136

import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
row = r//n
col = c//n
if (r%n):
    row += 1
if (c%n):
    col += 1
    
print(row * col)