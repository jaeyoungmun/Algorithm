import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

def bfs(v):
    q = deque([(v, 0)])
    visited = set()
    while q:
        # print('q',q)
        x, count = q.popleft()
        # print('x와 count',x, count)

        if x == 1:
            return count
        if x in visited:
            continue

        visited.add(x)

        if x % 3 == 0 and (x // 3) not in visited:
            q.append((x // 3, count + 1))
        if x % 2 == 0 and (x // 2) not in visited:
            q.append((x // 2, count + 1))
        if x - 1 not in visited:
            q.append((x - 1, count + 1))

print(bfs(n))