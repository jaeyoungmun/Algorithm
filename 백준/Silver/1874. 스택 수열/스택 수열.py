import sys
input = sys.stdin.readline

my_lst = [] # 수열을 삽입,삭제할 리스트
print_lst = [] # 출력할 + - 를 저장할 리스트
j = 0 # answer_lst의 인덱스
n = int(input())
answer_lst = [int(input()) for _ in range(n)]
for i in range(1,n+1):
    my_lst.append(i)
    print_lst.append('+')
    while(answer_lst[j] == my_lst[-1]):
        my_lst.pop()
        print_lst.append('-')
        j += 1
        if not my_lst:
            break 
if my_lst:
    print("NO")
else:
    for i in range(len(print_lst)): # print_lst에 저장된 + - 를 출력
        print(print_lst[i])