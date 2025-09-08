n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
print(graph)
visited = [[False] * n for _ in range(n)]
print(visited)
count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    global count
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1 and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)

result = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            count = 0
            dfs(i, j)
            result.append(count)

print(len(result))
for tem in result:
    print(tem)