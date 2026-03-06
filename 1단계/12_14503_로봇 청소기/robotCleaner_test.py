n, m = map(int, input().split())
r, c, d = map(int, input().split())
map = [list(map(int,input().split())) for _ in range(n)]
count = 0
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

for i in range(n):
    print(map[i])

while True:
    if map[r][c] == 0:
        map[r][c] = 2
        count += 1

    clean_flag = False
    # 현재 칸 주변 4방향 탐색
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        # 청소할 칸이 있다
        if map[nr][nc] == 0:
            clean_flag = True

    # 청소할 칸이 있으면
    if clean_flag:
        d = (d +3) % 4
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < m and map[nr][nc] == 0:
            r, c = nr, nc
    # 청소할 칸이 없으면
    else:
        nd = (d + 2) % 4
        nr, nc = r + dr[nd], c + dc[nd]
        if 0 <= nr < n and 0 <= nc < m and map[nr][nc] != 1:
            r, c = nr, nc
        else:
            break
print(count)