from collections import deque

n, m, v = map(int, input().split())
print(f"n:{n} m:{m} v:{v}")

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i].sort()
print(graph)

def dfs(v, visited):
    print(v, end=' ')
    visited[v] = True
    for next_node in graph[v]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, visited)

visited_dfs = [False] * (n+1)
dfs(v, visited_dfs)

print()

def bfs(v, visited):
    queue = deque()
    queue.append(v)
    while queue:
        now = queue.popleft()
        visited[now] = True
        print(now, end=' ')
        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

visited_bfs = [False] * (n+1)
bfs(v, visited_bfs)