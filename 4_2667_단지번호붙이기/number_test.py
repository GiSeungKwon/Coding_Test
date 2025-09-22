n = int(input())

graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
count = 0
result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    global count
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            result.append(count)
            count = 0

print(len(result))
for item in result:
    print(item)