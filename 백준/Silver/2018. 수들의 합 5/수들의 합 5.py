n = int(input())

answer = 1 # n이 홀로 자기자신만 있는 경우 미리 삽입

i = 1 # 시작인덱스
j = 1 # 끝인덱스
sum = 1 # i~j의 수들의 합

while(j < n):
    if (sum == n): # 연속된 수의 합이 n과 같은 경우
        j += 1
        sum += j
        answer += 1
    elif (sum > n): # 연속된 수의 합이 n보다 커진 경우
        sum -= i
        i+= 1
    elif (sum < n): # 연속된 수의 합이 n보다 작은 경우
        j += 1
        sum += j

print(answer)