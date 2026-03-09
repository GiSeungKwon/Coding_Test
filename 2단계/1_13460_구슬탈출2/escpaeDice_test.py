from collections import deque

n, m = map(int, input().split())
map = [list(input().strip()) for _ in range(n)]

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

red, blue = [], []
for i in range(n):
    for j in range(m):
        if