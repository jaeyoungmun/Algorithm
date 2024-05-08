import sys
input = sys.stdin.readline

len_s, len_p = map(int, input().split())
S = input()
check_arr = list(map(int, input().split())) # P에 포함돼야 할 각 문자의 갯수
answer_arr = [0,0,0,0] # 각 dna문자열의 갯수 현황
answer = 0 # 각 dna문자열의 조건부합 여부 기록
result = 0 # 출력할 수

def add(i): # 새로 들어온 문자를 체크하고 정답상태 업데이트하는 함수
    global answer
    if i == 'A':
        answer_arr[0] += 1
        if answer_arr[0] == check_arr[0]:
            answer += 1
    elif i == 'C':
        answer_arr[1] += 1
        if answer_arr[1] == check_arr[1]:
            answer += 1
    elif i == 'G':
        answer_arr[2] += 1
        if answer_arr[2] == check_arr[2]:
            answer += 1
    elif i == 'T':
        answer_arr[3] += 1
        if answer_arr[3] == check_arr[3]:
            answer += 1
def remove(i): # 마지막 문자를 제거하고 answer_arr상태 업데이트하는 함수
    global answer
    if i == 'A':
        if answer_arr[0] == check_arr[0]:
            answer -= 1
        answer_arr[0] -= 1
    elif i == 'C':
        if answer_arr[1] == check_arr[1]:
            answer -= 1
        answer_arr[1] -= 1
    elif i == 'G':
        if answer_arr[2] == check_arr[2]:
            answer -= 1
        answer_arr[2] -= 1
    elif i == 'T':
        if answer_arr[3] == check_arr[3]:
            answer -= 1
        answer_arr[3] -= 1

for i in range(4):
    if check_arr[i] == 0:
        answer += 1

for i in range(len_p): # 첫번째 P에 대한 조건검사
    add(S[i])
if answer == 4:
    result += 1

for i in range(len_p,len_s): 
    j = i-len_p # 문자열 중 첫번째문자
    add(S[i])
    remove(S[j])
    if (answer == 4):
        result += 1
print(result)