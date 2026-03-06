n, m = map(int, input().split())
r, c, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
    if map[r][c] == 0:
        map[r][c] = 2

    for i in range(4):
        nr, nc = r+dr[i], r+dc[i]