from collections import deque

m, n, h = map(int, input().split())
graph = [[[0]*m for _ in range(n)] for _ in range(h)]
for h_ in range(h):
    for n_ in range(n):
        graph[h_][n_] = list(map(int, input().split()))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()
for h_ in range(h):
    for n_ in range(n):
        for m_ in range(m):
            if graph[h_][n_][m_] == 1:
                queue.append((h_, n_, m_))

while queue:
    z, y, x = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0<=nx<m and 0<=ny<n and 0<=nz<h and graph[nz][ny][nx] == 0:
            graph[nz][ny][nx] = graph[z][y][x] + 1
            queue.append((nz, ny, nx))

days = 0
for h_ in range(h):
    for n_ in range(n):
        for m_ in range(m):
            days = max(days, graph[h_][n_][m_])
print(days-1 )