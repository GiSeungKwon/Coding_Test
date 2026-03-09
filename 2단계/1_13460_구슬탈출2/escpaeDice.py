from collections import deque

n, m = map(int, input().split())
map = [list(input().strip()) for _ in range(n)]
for i in range(n): print(map[i])
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
# 북동남서
dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]

def move(flag, r, c, dr, dc):
    count = 0
    while map[r + dr][c + dc] != '#' and map[r + dr][c + dc] == 'O':
        count += 1
        r += dr
        c += dc
    return r, c, count

red, hole, blue = [], [], []
for i in range(m):
    for j in range(n):
        if map[i][j] == 'R': red = [i, j]
        elif map[i][j] == 'O': hole = [i, j]
        elif map[i][j] == 'B': blue = [i, j]
print(f"red:{red}, hole:{hole}, blue:{blue}")
visited[red[0]][red[1]][blue[0]][blue[1]] = True
count = 0
queue = deque()
queue.append((red[0], red[1], blue[0], blue[1], count))
while queue:
    red_r, red_c, blue_r, blue_c, count = queue.popleft()
    for i in range(4):
        # red: 1, blue: -1
        next_red_r, next_red_c, red_count = move(1, red_r, red_c, dr[i], dc[i])
        next_blue_r, next_blue_c, blue_count = move(-1, blue_r, blue_c, dr[i], dc[i])
        if map[next_blue_r][next_blue_c] == 'O':
            continue
        if map[next_red_r][next_red_c] == 'O':
            print(count+1)
            exit()
        if not visited[next_red_r][next_red_c][next_blue_r][next_blue_c]:
            queue.append((next_red_r, next_red_c, next_blue_r, next_blue_c, count+1))