import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) # 재귀 깊이 설정

check_near_x = [-1, 1, 0, 0]
check_near_y = [0, 0, -1, 1]

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False 
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4):
            dfs(x+check_near_x[i], y+check_near_y[i])
        return True
    return False

T = int(input())
for _ in range(T):
    # 그래프 세팅
    graph = []
    count = 0
    m, n, k = map(int, input().split())
    for _ in range(n):
        graph.append([0 for _ in range(m)])
    # print(graph)
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    # print(graph)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                if dfs(i,j):
                    count += 1
                    # print('i,j출력: ',i,j)
    print(count)
    
