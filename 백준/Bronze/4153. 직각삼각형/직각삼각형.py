import sys
input = sys.stdin.readline

while(1):
    a, b, c = map(int, input().split())
    if a+b+c ==0:
        break
    max_c = max(a,b,c)
    if max_c == a:
        other_sides = b, c
    elif max_c == b:
        other_sides = a, c
    else:
        other_sides = a, b
    c2 = other_sides[0]**2 + other_sides[1]**2
    if c2 == (max_c**2):
            print('right')
    else:
        print('wrong')

