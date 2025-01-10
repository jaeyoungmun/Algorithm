import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [0 for _ in range(n)]
answer = []
for i in range(n):
	lst[i] = input()
# print(lst)
for i in range(n-7):
	for j in range(m-7):
		w_idx = 0 #흰색 시작
		b_idx = 0 #검은색 시작
		for a in range(i,i+8):
			for b in range(j,j+8):
				if (a+b)%2==0:
					if lst[a][b] != 'W':
						w_idx += 1
					else:
						b_idx += 1
				else:
					if lst[a][b] != 'W':
						b_idx += 1
					else:
						w_idx += 1
		answer.append(b_idx)
		answer.append(w_idx)
print(min(answer))
