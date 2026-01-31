from collections import deque

n, m, v = map(int, input().split())
print(n, m, v)

graph = [[] for _ in range(n+1)]
print(graph)

for _ in range(m):
    start, end = map(int, input().split())
    print(f"start:{start} end:{end}")
    graph[start].append(end)
    graph[end].append(start)
print(graph)

for i in range(n):
    graph[i].sort()
print(graph)

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

def dfs(v, visited):
    print(v, end=" ")
    visited[v] = True
    for nnode in graph[v]:
        if not visited[nnode]:
            visited[nnode] = True
            dfs(nnode, visited)

def bfs(v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        print(now, end=" ")
        for nnode in graph[now]:
            if not visited[nnode]:
                visited[nnode] = True
                queue.append(nnode)

dfs(v, visited_dfs)
print()
bfs(v, visited_bfs)