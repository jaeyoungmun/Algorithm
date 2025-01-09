import sys
input = sys.stdin.readline

a,b = map(int, input().split())
lst = [i for i in range(1,11)] * 2 # 시작할때의 카드더미를 리스트화
lst.sort()

def couple_of_number(num):
    # print(18*17//2) # 18C2 => 상대가 뽑았을 카드의 전체경우의 수: 153
    answer = 1-((10-num)/153)
    print("%.3f" %answer)

def another_number(a,b):
    answer = 0 # 내가 이기는 경우의 수
    count = 0 # 상대가 뽑았을 카드의 모든 경우의 수
    lst.remove(a)
    lst.remove(b)
    # print(lst)
    my_num = (a + b) % 10 #내 족보 ex. 1,2라면 3끗
    # print("내 족보: ",my_num)
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            count += 1
            if (lst[i]+lst[j]) % 10 < my_num:
                if lst[i] != lst[j]:
                    answer += 1
    print("%.3f" %(answer/count))

# 땡을 뽑았을 경우
if a == b:
    couple_of_number(a)

# 끗을 뽑았을 경우
else:
    another_number(a,b)