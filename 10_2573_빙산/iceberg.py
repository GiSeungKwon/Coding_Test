from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

def melt():
    melt_graph = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                sea = 0
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if 0<=ni<n and 0<=nj<m and graph[ni][nj] == 0:
                        sea += 1
                melt_graph[i][j] = sea

    for i in range(n):
        for j in range(m):
            graph[i][j] = max(0, graph[i][j]-melt_graph[i][j])

result = []
year = 0
while True:
    count = 0
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j]>0:
                bfs(i, j, visited)
                count += 1
    result.append(count)
    if count == 0:
        print(0)
        break
    if count >= 2:
        print(year)
    melt()
    year+=1
print(result)