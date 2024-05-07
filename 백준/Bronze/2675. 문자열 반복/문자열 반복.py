import sys
input = sys.stdin.readline

n = int(input())
def P(r,s):
    p = ""
    for i in range(len(s)):
        p += s[i]*r
    print(p)

for _ in range(n):
    r, s = map(str,input().split())
    r = int(r)
    P(r,s)