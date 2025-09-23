from collections import deque

# 입력
m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 좌우 앞뒤 상하
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    queue = deque()
    # 익은 토마토 위치 저장
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if box[z][y][x] == 1:
                    queue.append((z, y, x))

    # BFS
    while queue:
        z, y, x = queue.popleft()
        for d in range(6):
            nz, ny, nx = z + dz[d], y + dy[d], x + dx[d]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = box[z][y][x] + 1
                    queue.append((nz, ny, nx))

    # 결과 확인
    days = 0
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if box[z][y][x] == 0:  # 익지 않은 토마토 존재
                    return -1
                days = max(days, box[z][y][x])
    return days - 1  # 첫날은 1로 시작했으니 -1


# 실행
print(bfs())
