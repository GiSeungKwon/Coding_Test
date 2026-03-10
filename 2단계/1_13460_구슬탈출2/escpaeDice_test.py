from collections import deque
n, m = map(int, input().split())
map = [list(input().strip()) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

red, blue = [], []
for i in range(n):
    for j in range(m):
        if map[i][j] == 'R': red = [i, j]
        if map[i][j] == 'B': blue = [i, j]

count = 0
queue = deque()
queue.append([red[0], red[1], blue[0], blue[1], count])
visited [red[0]] [red[1]] [blue[0]] [blue[1]] = True

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def move(r, c, dr, dc):
    count = 0
    while map[r+dr][c+dc] != '#':
        r += dr
        c += dc
        count += 1
        if map[r][c] == 'O':
            break
    return r, c, count

flag = False
while queue:
    now_red_r, now_red_c, now_blue_r, now_blue_c, count = queue.popleft()
    if 10 <= count:
        break

    for i in range(4):
        next_red_r, next_red_c, red_count = move(now_red_r, now_red_c, dr[i], dc[i])
        next_blue_r, next_blue_c, blue_count = move(now_blue_r, now_blue_c, dr[i], dc[i])
        if map[now_blue_r][now_blue_c] == 'O':
            continue
        if map[now_red_r][now_red_c] == 'O':
            flag = True
            break
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
if flag:
    print(count+1)
else:
    print(-1)