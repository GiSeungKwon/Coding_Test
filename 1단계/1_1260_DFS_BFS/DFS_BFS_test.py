from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        print(now, end=" ")
        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

def dfs(v, visited):
    print(v, end=" ")
    visited[v] = True
    for next_node in graph[v]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, visited)

visited_bfs = [False] * (n+1)
visited_dfs = [False] * (n+1)
bfs(v, visited_bfs)
print()
dfs(v, visited_dfs)