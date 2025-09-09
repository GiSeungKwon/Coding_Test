from collections import deque

# 입력
m, n, h = map(int, input().split())
box = [[[0]*m for _ in range(n)] for _ in range(h)]

for k in range(h):
    for i in range(n):
        box[k][i] = list(map(int, input().split()))

# 좌우 앞뒤 상하
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 익은 토마토 위치 저장
queue = deque()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 1:
                queue.append((z, y, x))

# BFS
while queue:
    z, y, x = queue.popleft()
    for d in range(6):
        nz = z + dz[d]
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
            if box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[z][y][x] + 1
                queue.append((nz, ny, nx))

# 결과 확인
days = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 0:
                print(-1)
                exit()
            days = max(days, box[z][y][x])

print(days - 1)  # 첫날은 1로 시작했으니 -1
