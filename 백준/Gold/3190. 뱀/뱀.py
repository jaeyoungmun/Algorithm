import sys
input = sys.stdin.readline
from collections import deque

def main():
    N = int(input().strip())
    K = int(input().strip())
    apples = set()
    for _ in range(K):
        r, c = map(int, input().split())
        apples.add((r-1, c-1))

    L = int(input().strip())
    turns = {}
    for _ in range(L):
        t, d = input().split()
        turns[int(t)] = d

    dirs = [(0,1),(1,0),(0,-1),(-1,0)]  # right, down, left, up
    dir_idx = 0  # start facing right

    snake = deque()
    snake.append((0,0))
    snake_set = {(0,0)}

    time = 0
    while True:
        time += 1
        head_r, head_c = snake[-1]
        dr, dc = dirs[dir_idx]
        nr, nc = head_r + dr, head_c + dc

        # check wall collision
        if not (0 <= nr < N and 0 <= nc < N):
            print(time)
            return

        # check self collision
        if (nr, nc) in snake_set:
            print(time)
            return

        # move head
        snake.append((nr, nc))
        snake_set.add((nr, nc))

        # apple?
        if (nr, nc) in apples:
            apples.remove((nr, nc))
        else:
            # move tail
            tail = snake.popleft()
            snake_set.remove(tail)

        # apply turn if exists after this second
        if time in turns:
            if turns[time] == 'L':
                dir_idx = (dir_idx - 1) % 4
            else:  # 'D'
                dir_idx = (dir_idx + 1) % 4

if __name__ == "__main__":
    main()
