n = int(input())
m = int(input())
count = 0
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)

def dfs(v, visited):
    global count
    count += 1
    visited[v] = True
    for next_node in graph[v]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, visited)
visited = [False] * (n+1)
dfs(1, visited)
print(count-1)