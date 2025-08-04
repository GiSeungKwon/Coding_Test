<<<<<<< HEAD
=======
from collections import deque

n, m = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(n)]
print(maze)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                queue.append([nx, ny])
                maze[nx][ny] = maze[x][y] + 1
    return maze[n-1][m-1]

print(bfs(0, 0))
>>>>>>> e1cc33a907a017d2e704dfb5fa6a93b05032ee51
