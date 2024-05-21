import sys
input = sys.stdin.readline

# l: 입력받는 문자열
# dic: 딕셔너리에 문자:횟수 형태로 키밸류
# max가 중복으로 있을경우를 어케 구분하지
l = input().upper().rstrip()
dic = {}
for i in range(len(l)):
    if l[i] not in dic:
        dic[l[i]] = 1
    elif l[i] in dic:
        dic[l[i]] += 1

# 최대 빈도수를 찾기
max_count = max(dic.values())

# 최대 빈도수를 가진 문자의 개수를 셈
max_chars = [char for char, count in dic.items() if count == max_count]

if len(max_chars) > 1:
    print('?')
else:
    print(max_chars[0])