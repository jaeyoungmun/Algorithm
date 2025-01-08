import sys
input = sys.stdin.readline

def tri_num(n):
    return n*(n+1) // 2

def check_answer(K):
    for i in range(1,45):
        for j in range(1,45):
            for k in range(1,45):
                if (tri_num(i) + tri_num(j) + tri_num(k)) == K:
                    return 1
    return 0
                
T = int(input())
for _ in range(T):
    K = int(input())
    # print(t(44)) #990

    answer = check_answer(K)
    print(answer)