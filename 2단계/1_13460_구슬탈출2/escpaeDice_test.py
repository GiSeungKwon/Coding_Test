from collections import deque

n, m = map(int, input().split())
map = [list(input().strip()) for _ in range(n)]
for i in range(n):
    print(map[i])
# 상하좌우
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
# R, O, B 좌표 구하기
red_coord, O_coord, blue_coord = [], [], []
for i in range(n):
    for j in range(m):
        if map[i][j] == 'R': red_coord = [i, j]
        elif map[i][j] == 'O': O_coord = [i, j]
        elif map[i][j] == 'B': blue_coord = [i, j]

count = 0
queue = deque()
queue.append([red_coord[0], red_coord[1], count])
flag = False

visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
# 초기 위치 방문 처리
visited[red_coord[0]][red_coord[1]][blue_coord[0]][blue_coord[1]] = True

queue = deque()
queue.append([(red_coord[0], red_coord[1], blue_coord[0], blue_coord[1], count)])

def move(r, c, dr, dc):
    count = 0
    while map[r + dr][c + dc] != '#' and map[r][c] != 'O':
        r += dr
        c += dc
        count += 1
    return r, c, count

# BFS 내부
while queue:
    ry, rx, by, bx, dist = queue.popleft()
    if dist >= 10: break

    for i in range(4):
        nry, nrx, r_cnt = move(ry, rx, dr[i], dc[i])
        nby, nbx, b_cnt = move(by, bx, dr[i], dc[i])

        # 파랑 빠지면 무시
        if map[nby][nbx] == 'O':
            continue

        # 빨강만 빠지면 성공!
        if map[nry][nrx] == 'O':
            print(dist + 1)
            exit()

        if nry == nby and nrx == nbx:  # 겹쳤을 때 처리
            if r_cnt > b_cnt:
                nry -= dr[i]; nrx -= dc[i]
            else:
                nby -= dr[i]; nbx -= dc[i]

        if not visited[nry][nrx][nby][nbx]:
            visited[nry][nrx][nby][nbx] = True
            queue.append((nry, nrx, nby, nbx, dist + 1))
