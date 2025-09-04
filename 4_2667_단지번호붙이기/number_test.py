n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
print(graph)

visited = [[False] * n for _ in range(n)]
print(visited)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
result = []

def dfs(x, y):
    global count
    count += 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and not visited[i][j]:
            count = 0
            dfs(i, j)
            result.append(count)

print(len(result))
for i in sorted(result):
    print(i)