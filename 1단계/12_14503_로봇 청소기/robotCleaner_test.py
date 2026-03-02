from collections import deque

n, m = map(int, input().split())
print(f"n:{n}, m:{m}")
y, x, d = map(int, input().split())
print(f"y:{y}, x:{x}, d:{d}")
dy, dx = [-1,0,1,0], [0,1,0,-1]
graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    print(graph[i])
visited = [[False] * m for _ in range(n)]
for i in range(n):
    print(visited[i])

queue = deque()
queue.append((y, x, d))
while queue:
    y, x, d = queue.popleft()
    flag_clean = False
    # 북동남서 청소가 필요한 칸이 있는지 확인
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<n and 0<=nx<m:
            # 청소가 필요한 칸이 있으면 flag_clean = True
            if graph[ny][nx] == 0:
                flag_clean = True
                break

    if flag_clean:
        nd = (d + 3) % 4
        ny, nx = y + dy[nd], x + dx[nd]
        if graph[ny][nx] == 0 and not visited[ny][nx]:
            visited[ny][nx] = True
            graph[ny][nx] = "-"
            queue.append((ny, nx, d))
    else:
        nd = (d + 2) % 4
        ny, nx = y + dy[nd], x + dx[nd]
        if graph[ny][nx] != 1:
            visited[ny][nx] = True
            graph[ny][nx] = "-"
            queue.append((ny, nx, d))
        else:
            break
