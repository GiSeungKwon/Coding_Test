from collections import deque

# 입력
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 간선 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호 작은 순으로 방문하기 위해 정렬
for g in graph:
    g.sort()

# DFS 구현
def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for u in graph[v]:
        if not visited[u]:
            dfs(u, visited)

# BFS 구현
def bfs(v):
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for u in graph[now]:
            if not visited[u]:
                visited[u] = True
                queue.append(u)

# 실행
dfs_visited = [False] * (n + 1)
dfs(v, dfs_visited)
print()
bfs(v)
