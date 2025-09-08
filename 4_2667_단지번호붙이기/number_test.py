n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
print(graph)
visited = [[False]*n for _ in range(n)]
print(visited)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            global count
            count += 1
            visited[nx][ny] = True
            dfs(nx, ny)

result = []

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            result.append(count)
            count = 0

print(len(result))
for i in range(len(result)):
    print(result[i])