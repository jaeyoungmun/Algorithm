import sys
input = sys.stdin.readline

a,b = map(int,input().split())

def answer(a,b):
    a2 = a*a
    b2 = b*b
    return a2 - b2
print(answer(a,b))