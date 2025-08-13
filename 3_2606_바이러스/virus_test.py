n = int(input())
m = int(input())
print(n, m)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
for i in range(n+1):
    graph[i].sort()
print(graph)

count = 0

visited = [False] * (n+1)
def dfs(v):
    global count
    count += 1
    visited[v] = True
    print(v, end = ' ')
    for next_node in graph[v]:
        if not visited[next_node]:
            dfs(next_node)
            visited[next_node] = True

dfs(1)
print()
print(count-1)