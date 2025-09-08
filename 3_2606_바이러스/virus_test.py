n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

print(graph)
count = 0
def dfs(v, visited):
    visited[v] = True
    global count
    count += 1
    for next_node in graph[v]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, visited)
visited = [False] * (n+1)
dfs(1, visited)
print(count-1)