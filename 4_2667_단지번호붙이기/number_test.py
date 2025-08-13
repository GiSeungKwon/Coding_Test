n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0

def dfs(x, y):
    global count
    count += 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)

result = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0

len_result = len(result)
print(len_result)
for i in range(len_result):
    print(result[i])