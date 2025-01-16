import sys
input = sys.stdin.readline

n = int(input())
T = []  # 상담에 걸리는 기간
P = []  # 상담료
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# 상담하기 함수 정의
def working(start, end):
    max_profit = 0
    # 기간 내 가능한 모든 상담을 고려
    for i in range(start, end):
        if i + T[i] <= end:  # 상담이 가능한 경우
            profit = P[i]  # 현재 상담의 이익
            # 다음 상담을 재귀적으로 호출하여 최대 이익 계산
            next_profit = working(i + T[i], end)
            max_profit = max(max_profit, profit + next_profit)
    return max_profit

# 전체 기간에 대해 최대 이익 계산
max_money = working(0, n)
print(max_money)