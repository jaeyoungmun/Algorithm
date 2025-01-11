def find_squre(s):
    for i in range(n-s+1): # 행
        for j in range(m-s+1): # 열
            if input_lst[i][j] == input_lst[i][j+s-1] == input_lst[i+s-1][j] == input_lst[i+s-1][j+s-1]:
                return True

    return False


n,m = map(int,input().split())
input_lst = []
for _ in range(n):
    input_lst.append(input())
# print(input_lst[0][3])

size = min(n,m)

# 가장 큰 정사각형을 구해야 하므로 최대 크기부터 하나씩 줄여가며 시작
for k in range(size, 0, -1):
    # 네 꼭지점의 크기가 같은 정사각형을 찾았으면 True를 받아 넓이를 출력해주고 break
    if find_squre(k):
        print(k**2)
        break