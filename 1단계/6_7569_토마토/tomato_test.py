from collections import deque

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
print(graph)
# visited = [[[False] * m for _ in range(n)] for _ in range(h)]
# print(visited)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    queue = deque()
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if graph[z][y][x] == 1:
                    queue.append((z, y, x))
                    # visited[z][y][x] = True
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nz, ny, nx = z+dz[i], y+dy[i], x+dx[i]
            if 0<=nz<h and 0<=ny<n and 0<=nx<m and graph[nz][ny][nx] == 0:
                # visited[nz][ny][nx] = True
                queue.append((nz, ny, nx))
                graph[nz][ny][nx] = graph[z][y][x] + 1
    days = 0
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if graph[z][y][x] == 0:
                    return -1
                days = max(days, graph[z][y][x])
    return days-1

print(bfs())