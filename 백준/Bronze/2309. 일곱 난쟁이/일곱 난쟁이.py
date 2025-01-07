import sys
input = sys.stdin.readline

lst = [int(input()) for _ in range(9)]
sum = sum(lst)
def find_100():
    for i in range(8):
        for j in range(i+1,9):
            answer = sum - lst[i] - lst[j]
            # print(answer)
            if answer == 100:
                # print("answer가 100이됨=> ",lst)
                a = lst[i] #첫번째 가짜 난쟁이
                b = lst[j] #두번째 가짜 난쟁이
                lst.remove(a)
                lst.remove(b)
                lst.sort()
                # print(lst)
                return 
find_100()
for i in lst:
    print(i)