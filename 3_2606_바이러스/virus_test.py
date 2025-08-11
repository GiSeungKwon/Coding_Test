n = int(input())
m = int(input())
count = 0

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
print(visited)

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(n+1):
    graph[i].sort()
print(graph)

def dfs(v):
    visited[v] = True
    print(v, end = ' ')
    global count
    count += 1
    for next_node in graph[v]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node)

dfs(1)
print()
print(count-1)