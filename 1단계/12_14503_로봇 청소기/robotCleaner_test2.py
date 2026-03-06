n, m = map(int, input().split())
print(f"n:{n}, m:{m}")
r, c, d = map(int, input().split())
print(f"r:{r}, c:{c}, d:{d}")
map = [list(map(int, input().split())) for _ in range(n)]
count = 0

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
    if map[r][c] == 0:
        map[r][c] = 2
        count += 1
        for i in range(n):
            print(map[i])
        print()

    clean_flag = False
    # 현재 칸의 4방향 탐색
    for i in range(4):
        nr, nc = r+dr[i], r+dc[i]
        if 0<=nr<n and 0<=nc<m and map[nr][nc] == 0:
            clean_flag = True

    # 청소할 칸이 있다
    if clean_flag:
        d = (d + 3) % 4
        nr, nc = r+dr[d], c+dc[d]
        if 0<=nr<n and 0<=nc<m and map[nr][nc] == 0:
            r, c = nr, nc

    #청소할 칸이 없다
    else:
        back_d = (d + 2) % 4
        back_r, back_c = r + dr[back_d], c + dc[back_d]
        if 0<=back_r<n and 0<=back_c<m and map[back_r][back_c] != 1:
            r, c = back_r, back_c
        elif 0<=back_r<n and 0<=back_c<m and map[back_r][back_c] == 1:
            print("정지")
            break
print(count)