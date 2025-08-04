count = 0

def dfs(v, visited):
    global count
    visited[v] = True
    print(v, end = ' ')
    for next_node in graph[v]:
        if not visited[next_node]:
            count += 1
            visited[next_node] = True
            dfs(next_node, visited)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(n+1):
    graph[i].sort()

print(graph)
visited = [False] * (n+1)
dfs(1, visited)
print()
print(count)