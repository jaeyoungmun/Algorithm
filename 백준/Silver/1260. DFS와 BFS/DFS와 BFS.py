import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

temp = []
dic = {}
dfs_answer = []
bfs_answer = []
for _ in range(m):
    temp.append(list(map(int, input().split())))

# print(dic)
# print(temp[0][1])

# 간선의 개수만큼 for문 돌려서 일단 저장하고 이후에 root를 기준으로 정렬하자
for i in temp:
    if i[0] in dic:
        dic[i[0]].append(i[1])
    else:
        dic[i[0]] = [(i[1])]

    if i[1] in dic:
        dic[i[1]].append(i[0])
    else:
        dic[i[1]] = [i[0]]
# print(dic)
for i in dic:
    dic[i].sort()

# DFS 구현
def dfs(r):
    dfs_answer.append(r)
    for neighbor in dic.get(r, []):
        if neighbor not in dfs_answer:
            dfs(neighbor)

# BFS 구현
def bfs(start):
    bfs_answer.append(start)
    visited = {start}  # 방문한 노드 집합
    current_level = [start]  # 현재 레벨의 노드들

    while current_level:
        next_level = []  # 다음 레벨의 노드들
        for node in current_level:
            for neighbor in dic.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)  # 방문 처리
                    next_level.append(neighbor)  # 다음 레벨에 추가
        bfs_answer.extend(next_level)  # 다음 레벨의 노드들을 결과에 추가
        current_level = next_level  # 현재 레벨을 다음 레벨로 업데이트

# DFS 수행
dfs(v)
for i in dfs_answer:
    print(i, end=' ')
print()

# BFS 수행
bfs(v)
for i in bfs_answer:
    print(i, end=' ')
