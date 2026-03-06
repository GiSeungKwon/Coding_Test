n, m = map(int, input().split())
r, c, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
count = 0
# 북 동 남 서 / dr[d], dc[d] 현재 방향을 나타냄
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
exit_flag = False

while True:
    if exit_flag:
        break
    # 현재 칸 청소 됨?
    if map[r][c] == 0:
        # 현재 칸 청소
        map[r][c] = 2
        count += 1

    clean_flag = False
    # 주변 4칸 탐색
    for i in range(4):
        check_r, check_c = r+dr[i], c+dc[i]
        # 청소 안된 칸 있음
        if map[check_r][check_c] == 0:
            clean_flag = True

    if clean_flag:
        # 반시계 방향 90도
        d = (d + 3) % 4
        # 진행 방향 칸이 청소 안된 칸이면 전진
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < m and map[nr][nc] == 0:
            r, c = nr, nc
            continue
    else:
        # 후진 방향
        nd = (d + 2) % 4
        nr, nc = r + dr[nd], c + dc[nd]
        # 진행 방향 칸이 벽이면
        if 0 <= nr < n and 0 <= nc < m and map[nr][nc] == 1:
            exit_flag = True
        # 후진 가능하면
        else:
            r, c = nr, nc