from collections import deque

n, m = map(int, input().split())
end_y, end_x = n-1, m-1

visited = [[False]*m for _ in range(n)]
maze = [list(map(int, input().strip())) for _ in range(n)]

# maze = [[-1]*m for _ in range(n)]
# for i in range(n):
#     str = input().strip()
#     for j in range(m):
#         maze[i][j] = int(str[j])

for i in range(n):
    print(maze[i])

# 상하좌우
dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]

#BFS - y, x, move
queue = deque([(0,0,1)])
while queue:
    y, x, move = queue.popleft()
    visited[y][x] = True

    if y == end_y and x == end_x:
        print(move)
        break

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0<=ny<n and 0<=nx<m and maze[ny][nx] == 1:
            if not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx, move+1))