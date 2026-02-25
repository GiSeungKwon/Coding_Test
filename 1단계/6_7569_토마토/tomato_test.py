from collections import deque
m, n, h = map(int, input().split())
print(f"m:{m}, n:{n}, h:{h}")

graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# for i in range(h):
#     for j in range(n):
#         print(f"graph[{i}][{j}]: {graph[i][j]}")

visited = [[[False]*m for _ in range(n)] for _ in range(h)]
# for i in range(h):
#     for j in range(n):
#         print(f"visited[{i}][{j}]: {visited[i][j]}")

def solution(m,n,h,graph):
    dz = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dx = [0, 0, 0, 0, -1, 1]

    flag = True
    for z in range(h):
        for y in range(n):
            if 0 in graph[z][y]:
                flag = False
    if flag:
        return 0

    max_count = 0
    queue = deque()
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if graph[z][y][x] == 1:
                    visited[z][y][x] = True
                    queue.append((z,y,x,0))
    print(f"queue: {queue}")
    while queue:
        z, y, x, count = queue.popleft()
        print(f"queue.popleft() -> z:{z}, y:{y}, x:{x}, count:{count}")
        max_count = max(max_count, count)
        for i in range(6):
            nz, ny, nx = z+dz[i], y+dy[i], x+dx[i]
            if 0<=nz<h and 0<=ny<n and 0<=nx<m and graph[nz][ny][nx] != -1:
                if not visited[nz][ny][nx]:
                    visited[nz][ny][nx] = True
                    print(f"queue.append((nz:{nz}, ny:{ny}, nx:{nx}, count + 1:{count + 1}))")
                    queue.append((nz, ny, nx, count + 1))
                    print(f"queue: {queue}")
                    print()
    return max_count

print(solution(m,n,h,graph))