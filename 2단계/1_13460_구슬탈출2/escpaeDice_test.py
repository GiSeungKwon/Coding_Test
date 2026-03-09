from collections import deque

n, m = map(int, input().split())
map = [list(input().strip()) for _ in range(n)]
for i in range(n): print(map[i])
visited = [[[[[False] * m] for _ in range(n)] for _ in range(m)] for _ in range(n)]
# 북동남서
dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]

def move(r, c, dr, dc):
    while map[r][c] != '#':

red, hole, blue = [], [], []
for i in range(m):
    for j in range(n):
        if map[i][j] == 'R': red = [i, j]
        elif map[i][j] == 'O': red = [i, j]
        elif map[i][j] == 'B': red = [i, j]
print(f"red:{red}, hole:{hole}, blue:{blue}")

count = 0
queue = deque()
queue.append((red[0], red[1], blue[0], blue[1], count))
while queue:
    red_r, red_c, blue_r, blue_c, count = queue.popleft()
    for i in range(4):
        next_red = move(red_r, red_c, dr[i], dc[i])