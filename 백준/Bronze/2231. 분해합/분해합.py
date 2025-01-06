import sys
input = sys.stdin.readline

N = int(input())
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0 #각 자릿수에 해당하는 숫자

sum = 0

for i in range(1,N+1):
    one += 1
    if one == 10:
        one = 0
        two += 1
    if two == 10:
        two = 0
        three += 1
    if three == 10:
        three = 0
        four += 1
    if four == 10:
        four = 0
        five += 1
    if five == 10:
        five = 0
        six += 1
    sum = i + one + two + three + four + five + six
    if sum == N:
        print(i)
        break
if sum > N:
    print(0)