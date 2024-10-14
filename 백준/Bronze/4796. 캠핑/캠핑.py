import sys
input = sys.stdin.readline
i =1
while(True):
    answer = 0
    l, p, v = map(int, input().split())
    temp = p -l
    if l==0 and p==0 and v==0:
        break
    while(v > l):
        answer += l
        v -= l
        v -= temp
        if v <= l and v >0:
            answer += v
    print("Case %d: %d"%(i,answer))
    i += 1
