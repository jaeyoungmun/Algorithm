import sys
input = sys.stdin.readline

bingo_lst = [] # 철수의의 빙교판
check_lst = [] # 사회자의 빙고판
answer_lst = [] # 정답체크할 빙고판

for _ in range(5):
    bingo_lst += [list(map(int,input().split()))]
for _ in range(5):
    check_lst += [list(map(int,input().split()))]
for _ in range(5):
    answer_lst += [list(0 for _ in range(5))]
# print('bingo\n',bingo_lst)
# print('check\n',check_lst)
# print('answer\n',answer_lst)
def bingo_game():
	check = 0 # 사회자가 부르는 숫자의 인덱스 체크
	bingo = 0 # 빙고 갯수 체크
	cross1 =0
	cross2 =0 # 대각선 체크 여부 확인인
	checked_row = []
	checked_col = []
	for i in range(5):
		for j in range(5):
			check += 1
			temp = check_lst[i][j]
			for a in range(5): # 사회자가 부르는 수 탐색
				for b in range(5):
					if temp == bingo_lst[a][b]:
						answer_lst[a][b] += 1 # 지운 숫자 체크

			for a in range(5):

				#가로줄 빙고 체크
				if a not in checked_row and all(answer_lst[a][b] == 1 for b in range(5)):
					# print('가로줄 빙고',a)
					bingo += 1
					checked_row.append(a)
				

				#세로줄 빙고 체크
				if a not in checked_col and all(answer_lst[b][a] == 1 for b in range(5)):
					# print('세로줄 빙고',a)
					bingo += 1
					checked_col.append(a)

				#대각선 빙고 체크
				if cross1 ==0 and all(answer_lst[b][b] ==1 for b in range(5)):
					# print('대각선 빙고 좌상단',a,b)
					bingo += 1
					cross1 += 1
					
				if cross2 ==0 and all(answer_lst[b][4-b] ==1 for b in range(5)):
					# print('대각선 빙고 우상단',a,b)
					bingo += 1
					cross2 += 1
					
				if bingo >= 3:
					print(check)
					return check
                    
bingo_game()
# print('bingo\n',bingo_lst)
# print('check\n',check_lst)
# print('answer\n',answer_lst)
