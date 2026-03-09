from collections import deque

n, m = map(int, input().split())
map = [list(input().strip()) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
red, blue = [], []
for i in range(n):
    for j in range(m):
        if map[i][j] == 'R': red = [i, j]
        elif map[i][j] == 'B': blue = [i, j]

def move(r, c, dr, dc):
    count = 0
    while map[r + dr][c + dc] != '#':
        r += dr
        c += dc
        count += 1
        if map[r][c] == 'O':
            break
    return r, c, count

count = 0
queue = deque()
queue.append([red[0], red[1], blue[0], blue[1], count])
visited[red[0]][red[1]][blue[0]][blue[1]] = True

flag = False
while queue:
    red_r, red_c, blue_r, blue_c, count = queue.popleft()
    if 10 <= count:
        break
    if map[blue_r][blue_c] == 'O':
        continue
    if map[red_r][red_c] == 'O':
        flag=True
        print(count)
        break
    for i in range(4):
        next_red_r, next_red_c, red_count = move(red_r, red_c, dr[i], dc[i])
        next_blue_r, next_blue_c, blue_count = move(blue_r, blue_c, dr[i], dc[i])
        if next_red_r == next_blue_r and next_red_c == next_blue_c:
            if red_count < blue_count:
                next_blue_r -= dr[i]
                next_blue_c -= dc[i]
            else:
                next_red_r -= dr[i]
                next_red_c -= dc[i]
        if not visited[next_red_r][next_red_c][next_blue_r][next_blue_c]:
            visited[next_red_r][next_red_c][next_blue_r][next_blue_c] = True
            queue.append([next_red_r, next_red_c, next_blue_r, next_blue_c, count + 1])
if not flag:
