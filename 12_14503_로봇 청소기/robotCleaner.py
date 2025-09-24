N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

while True:
    # 1. 현재 칸 청소
    if graph[r][c] == 0:
        graph[r][c] = 2  # 청소됨 표시
        count += 1

    # 2. 주변 4칸 확인
    moved = False
    for _ in range(4):
        d = (d + 3) % 4  # 반시계 방향 회전
        nx, ny = r + dx[d], c + dy[d]
        if graph[nx][ny] == 0:  # 청소 안 된 빈 칸
            r, c = nx, ny
            moved = True
            break

    if moved:
        continue

    # 3. 후진
    back = (d + 2) % 4
    bx, by = r + dx[back], c + dy[back]
    if graph[bx][by] == 1:  # 벽이면 종료
        break
    else:  # 벽이 아니면 후진
        r, c = bx, by

print(count)
