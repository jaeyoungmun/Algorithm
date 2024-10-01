# 10809번 문제 알파벳찾기
# a는 0번째
# 딕셔너리로 a:0, b:1

import sys
input = sys.stdin.readline
abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
answer = []
for i in range(26): #제출해야하는 리스트 값 초기화
    answer.append('-1')
    
dic = {}
for i in range(26): # 알파벳과 알파벳의 순서에 해당하는 숫자를 dic자료형으로 세팅
    dic[i] = abc[i]
    
s = input()
for i in range(26):
    temp = s.find(dic[i])
    # print(dic[i],"= ", s.find(dic[i])) 테스트용 print문
    answer[i] = temp

for i in range(26): #정답 제출
    print(int(answer[i]), end=' ')
