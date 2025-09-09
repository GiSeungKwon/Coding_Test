from collections import deque

m, n, h = map(int, input().split())
graph = [[[0]*m for _ in range(n)] for _ in range(h)]

for h in range(h):
    for n in range(n):
        graph[h][n] = list(map(int, input().split()))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(x, y, z):
    queue = deque()
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if graph[z][y][x] == 1:
                    queue.append((z,y,x))

    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=nz<h and 0<=ny<n and 0<=nx<m and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nz, ny, nx))

days = 0
