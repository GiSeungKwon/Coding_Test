n, m = map(int, input().split())
r, c, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
    if map[r][c] == 0:
        map[r][c] = 2

    clean_flag = False
    # 현재 칸의 4방향 탐색
    for i in range(4):
        nr, nc = r+dr[i], r+dc[i]
        if map[nr][nc] == 0:
            clean_flag = True
    # 청소할 칸이 있다
    if clean_flag:

    #청소할 칸이 없다
    else:
