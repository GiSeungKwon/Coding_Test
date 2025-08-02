from collections import deque

from h5py.h5o import visit

n, m, v = map(int, input().split())
print(f"n:{n}, m:{m}, v:{v}")

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
for i in range(n+1):
    graph[i].sort()
print(graph)

def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for next_node in graph[v]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, visited)

def bfs(v, visited):
    visited[v] = True
    queue = deque()
    queue.append(v)
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

visited_dfs = [False] * (n+1)
dfs(v, visited_dfs)
print()
visited_bfs = [False] * (n+1)
bfs(v, visited_bfs)