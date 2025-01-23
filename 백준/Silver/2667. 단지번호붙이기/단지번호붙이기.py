import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) # 재귀 깊이 설정

check_near_x = [-1, 1, 0, 0]
check_near_y = [0, 0, -1, 1]
answer = 1 #단지번호
def dfs(x,y):
    if x < 0 or x >= T or y < 0 or y >= T:
        return False 
    if graph[x][y] == '1':
        if visited[x][y] == 0:
            visited[x][y] += answer
            for i in range(4):
                dfs(x+check_near_x[i], y+check_near_y[i])
            return True
        return False

T = int(input())
graph = []
for i in range(T):
    # 그래프 세팅
    temp = input()
    graph.append(temp)
    visited = [[0]* T for _ in range(T)]
    # print(graph)
# print('gg',graph[0][1])

for i in range(T):
    for j in range(T):
        if graph[i][j] == '1':
            if dfs(i,j):
                answer += 1
                # print('i,j출력: ',i,j)

print(answer-1)
# print(visited)
count = [0 for _ in range(answer)]
for k in range(1,answer):
    for i in range(T):
        for j in range(T):
            if visited[i][j] == k:
                count[k] += 1
# sorted(count)
count.remove(0)
count.sort()
for i in range(answer-1):
    print(min(count))
    count.remove(min(count))