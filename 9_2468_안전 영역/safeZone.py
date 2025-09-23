from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_height = max(map(max, graph))  # 지역의 최대 높이
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, h, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] > h:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

answer = 0
for h in range(max_height + 1):  # 강수량 0 ~ 최대 높이
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                bfs(i, j, h, visited)
                count += 1
    answer = max(answer, count)

print(answer)