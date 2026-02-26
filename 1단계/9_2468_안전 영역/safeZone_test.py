from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dy, dx = [1,-1,0,0], [0,0,-1,1]

max_values = []
max_vale = 0

# 최대 값 추출 Logic
for m in range(n):
    max_values.append(max(graph[m]))
max_value = max(max_values)

list_count = []
# m: 비가 온 정도 -> m 이하이면 잠기는거
for rain in range(max_value + 1):
    print(f"rain: {rain}")
    # 물에 잠기면 0, 물에 안잠기면 1(안전 영역)
    rain_graph = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if rain < graph[i][j]:
                rain_graph[i][j] = 1
            else:
                visited[i][j] = True

    queue = deque()
    for i in range(n):
        for j in range(n):
            if rain_graph[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                queue.append((i, j))
                while queue:
                    y, x = queue.popleft()
                    for k in range(4):
                        ny, nx = y+dy[k], x+dx[k]
                        if 0<=ny<n and 0<=nx<n and rain_graph[ny][nx] == 1:
                            if not visited[ny][nx]:
                                visited[ny][nx] = True
                                queue.append((ny, nx))
                count += 1
    list_count.append(count)
print(f"list_count: {list_count}")
print(max(list_count))