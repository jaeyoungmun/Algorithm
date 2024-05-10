import sys
input = sys.stdin.readline

T = int(input())
# ps_lst = [] # 입력받는 괄호문자열 저장할 리스트
def check_ps(ps_lst): # ps가 올바른 괄호문자열인지 판별
    temp = []
    for i in range(len(ps_lst)-1):
        temp.append(ps_lst[i])
        if temp[-1] == ')':
            temp.pop()
            if temp: # 리스트가 비어있지 않은 경우
                temp.pop()
            elif not temp: # 리스트가 비어있는 경우
                return False
        # print(temp)
    if ('(' or ')') in temp:
        return False
    elif not temp:
        return True
    
for i in range(T):
    ps_lst = input()
    answer = check_ps(ps_lst)
    if answer == True:
        print("YES")
    else:
        print("NO")