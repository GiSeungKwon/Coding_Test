n = int(input())
m = int(input())
print(f"n:{n} m:{m}")

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)

count = 0
visited = [False] * (n+1)
print(visited)

def dfs(v):
    global count
    count += 1
    visited[v] = True
    # print(v, end = ' ')
    for next_node in graph[v]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node)

dfs(1)
print(count-1)