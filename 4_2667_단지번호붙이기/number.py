import sys
sys.setrecursionlimit(10000)

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    global count
    visited[x][y] = True
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

# 결과 저장
result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            count = 0
            dfs(i, j)
            result.append(count)

# 출력
print(len(result))
for r in sorted(result):
    print(r)
