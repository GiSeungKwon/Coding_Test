n = int(input())
m = int(input())
# print(f"n:{n}, m:{m}")

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
# print(graph)

count = 0

def dfs(v, visited):
    global count
    count += 1
    visited[v] = True
    for next_node in graph[v]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, visited)

visited_dfs = [False] * (n+1)
dfs(1, visited_dfs)
print(count-1)