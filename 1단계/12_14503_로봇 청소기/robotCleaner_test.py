n, m = map(int, input().split())
print(f"n:{n}, m:{m}")
r, c, d = map(int, input().split())
print(f"r:{r}, c:{c}, d:{d}")
map = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    print(map[i])

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
    # 현재 칸 청소 됨?
    if map[r][c] == 0:
        # 현재 칸 청소
        map[r][c] = "■"

    # 주변 4칸 탐색
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        # 청소 안된 칸 있음?
        if map[nr][nc] == 0:
            # 반시계 방향 90도 회전 후 앞칸이 청소 안된 칸이면 전진