from collections import deque
# n: 층 i, m: 호 j
n, m = map(int, input().split())
dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]
graph = [list(map(int, input().split())) for _ in range(n)]

def after_1_year(graph_ice):
    list_ice = []
    for i in range(n):
        for j in range(m):
            if graph_ice[i][j] != 0:
                count = 0
                for k in range(4):
                    ny, nx = i+dy[k], j+dx[k]
                    if 0<=ny<n and 0<=nx<m and graph_ice[ny][nx] == 0:
                        count += 1
                list_ice.append((i,j,count))
    for ice in list_ice:
        graph_ice[ice[0]][ice[1]] -= ice[2]
        if graph_ice[ice[0]][ice[1]] < 0:
            graph_ice[ice[0]][ice[1]] = 0
    return graph_ice

def bfs(param_graph):
    queue = deque()
    visited = [[False] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if param_graph[i][j] != 0:
                queue.append((i, j))
                visited[i][j] = True
                y, x = queue.popleft()
                for k in range(4):
                    ny, nx = y+dy[k], x+dx[k]
                    if 0<=ny<n and 0<=nx<m and param_graph[ny][nx] != 0:
                        if not visited[ny][nx]:
                            visited[ny][nx] = True
                            queue.append((ny, nx))
    return count

print()
print(graph)
graph = after_1_year(graph)
print(bfs(graph))
print()
print(graph)
