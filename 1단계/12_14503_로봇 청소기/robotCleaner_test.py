n, m = map(int, input().split()) # 행 열
r, c, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
# 현재 칸이 청소 되어 있는지 확인
idx = 1
y, x = r, c
while True:
    if map[r][c] == 0:
        map[r][c] = str(idx)+"■"
        idx += 1

    for i in range(n):
        print(map[i])

    flag_do_clean = False
    for i in range(4):
        # 사방의 방향 변수
        ny, nx = y+dy[i], x+dx[i]
        # 사방에 청소할 칸이 있으면 회전 후, 청소할 칸이라면 전진
        if map[ny][nx] == 0:
            flag_do_clean = True
            d = (d + 3) % 4
            tmp_y, tmp_x = y+dy[d], x+dx[d]
            if map[tmp_y][tmp_x] == 0:
                y, x = tmp_y, tmp_x

    # 사방에 청소할 칸이 없으면 후진
    if not flag_do_clean:
        # 후진을 위한 임시 변수
        tmp_d = (d + 2) % 4
        tmp_y, tmp_x =  y+dy[tmp_d], x+dx[tmp_d]
        # 후진할 칸이 벽이 아닐 때
        if map[tmp_y][tmp_x] != 1:
            y, x = tmp_y, tmp_x
        # 후진할 칸이 벽일 때
        else:
            break
