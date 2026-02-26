n, m = map(int, input().split())
dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]
graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    print(graph[i])

list_ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            count = 0
            for m in range(4):
                ny, nx = i+dy[m], j+dx[m]
                if 0<=ny<n and 0<=nx<m and graph[ny][nx] == 0:
                    count += 1
            list_ice.append((i,j,count))
print(list_ice)