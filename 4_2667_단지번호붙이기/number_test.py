n = int(input())
print(n)
count = 0
result = []

graph = [list(map(int, input().strip())) for _ in range(n)]
print(graph)
visited = [[False] * n for _ in range(n)]
print(visited)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global count
    count += 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] == 1:
            visited[nx][ny] = True
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0

len_result = len(result)
print(f"len_result: {len_result}")
for i in range(len_result):
    print(result[i])