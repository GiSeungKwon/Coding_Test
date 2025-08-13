from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
for i in range(n+1):
    graph[i].sort()

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

def dfs(v):
    visited_dfs[v] = True
    print(v, end = ' ')
    for next_node in graph[v]:
        if not visited_dfs[next_node]:
            visited_dfs[next_node] = True
            dfs(next_node)

def bfs(v):
    visited_bfs[v] = True
    queue = deque()
    queue.append(v)
    while queue:
        now = queue.popleft()
        print(now, end = ' ')
        for next_node in graph[now]:
            if not visited_bfs[next_node]:
                visited_bfs[next_node] = True
                queue.append(next_node)

dfs(v)
print()
bfs(v)