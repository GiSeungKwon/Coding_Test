n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0
while True:
    if graph[r][c] == 0:
        graph[r][c] = 2
        count += 1

    moved = False
    for _ in range(4):
        d = (d+3)%4
        nr, nc = r + dx[d], c + dy[d]
        if graph[nr][nc] == 0:
            r, c = nr, nc
            moved = True
            break

    if moved:
        continue

    bd = (d+2)%4
    br, bc = r+dx[bd], c+dy[bd]
    if graph[br][bc] == 1:
        break
    r, c= br, bc

print(count)