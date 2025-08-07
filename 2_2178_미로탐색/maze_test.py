from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dx[i]
            if 0<=nx<n and 0<=ny<m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append([nx, ny])
    return maze[n-1][m-1]
print(dfs(0, 0))