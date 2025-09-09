from collections import deque

# 입력
n = int(input())
a, b = map(int, input().split())
m = int(input())

# 그래프 초기화 (1-indexed)
graph = [[] for _ in range(n + 1)]

# 관계 저장 (양방향)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 방문 여부 및 촌수 저장
visited = [False] * (n + 1)
dist = [-1] * (n + 1)

# BFS 시작
queue = deque()
queue.append(a)
visited[a] = True
dist[a] = 0

while queue:
    now = queue.popleft()
    for next_node in graph[now]:
        if not visited[next_node]:
            visited[next_node] = True
            dist[next_node] = dist[now] + 1
            queue.append(next_node)

# 결과 출력
print(dist[b])