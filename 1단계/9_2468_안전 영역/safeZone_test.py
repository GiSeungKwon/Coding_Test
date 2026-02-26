from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
max_values = []
max_vale = 0

# 최대 값 추출 Logic
for i in range(n):
    max_values.append(max(graph[i]))
max_value = max(max_values)

rain_graph = [[0] * n for _ in range(n)]
# 물에 잠기면 0, 물에 안잠기면 1(안전 영역)

list_count = []
# m: 비가 온 정도 -> m 이하이면 잠기는거
for m in range(1, max_value + 1):
    print(f"m: {m}")
    count = 0
    for i in range(n):
        for j in range(n):
            if m < graph[i][j]:
                rain_graph[i][j] = 1
    print(f"rain_graph")
    for i in range(n):
        print(rain_graph[i])

    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        print(visited[i])