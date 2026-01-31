from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
for i in range(len(graph)):
    graph.sort()
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