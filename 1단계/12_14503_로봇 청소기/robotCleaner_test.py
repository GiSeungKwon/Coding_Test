n, m = map(int, input().split())
print(f"n:{n}, m:{m}")
r, c, d = map(int, input().split())
print(f"r:{r}, c:{c}, d:{d}")
map = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    print(map[i])
    print()

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
        map[r][c] = "■"
        count += 1
        for i in range(n):
            print(count)
            print(map[i])
            print()

    # 주변 4칸 탐색
    for i in range(4):
        check_r, check_c = r+dr[i], c+dc[i]
        # 청소 안된 칸 있음
        if map[check_r][check_c] == 0:
            # 반시계 방향 90도
            d = (d + 3) % 4
            # 진행 방향 칸이 청소 안된 칸이면 전진
            nr, nc = r+dr[d], c+dc[d]
            if map[nr][nc] == 0:
                r, c = nr, nc
                break
        # 창소 안된 칸 없음
        else:
            # 후진 방향
            d = (d + 2) % 4
            # 진행 방향 칸이 벽이면
            nr, nc = r+dr[d], c+dc[d]
            if map[nr][nc] == 1:
                exit_flag = True
                break
            # 후진 가능하면
            else:
                r, c = nr, nc
                break