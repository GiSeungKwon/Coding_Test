from collections import deque

n, m = map(int, input().split())
map = [list(input().strip()) for _ in range(n)]

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

red, blue = [], []
for i in range(n):
    for j in range(m):
        if map[i][j] == 'R': red = [i, j]
        elif map[i][j] == 'B': blue = [i, j]

def move(r, c, dr, dc):
    count = 0
    while map[r+dr][c+dc] != '#':
        r += dr
        c += dc
        count += 1
        if map[r][c] == 'O':
            break
    return r, c, count

count = 0
queue = deque()
queue.append([red[0], red[1], blue[0], blue[1], count])

while queue:
    now_red_r, now_red_c, now_blue_r, now_blue_c, count = queue.popleft()
    for i in range(4):
        next_red_r, next_red_c, red_count = move(now_red_r, now_red_c, dr[i], dc[i])
        next_blue_r, next_blue_c, blue_count = move(now_blue_r, now_blue_c, dr[i], dc[i])
        if map[next_red_r][next_red_c] == 'O':
            print()
        if not visited[next_red_r][next_red_c][next_blue_r][next_blue_c]:
            visited[next_red_r][next_red_c][next_blue_r][next_blue_c] = True
            queue.append([next_red_r, next_red_c, next_blue_r, next_blue_c, count + 1])
print(-1)