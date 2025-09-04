n = int(input())
start, end = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

print(graph)

visited = [False] * (n+1)
count = 0

def dfs(start, end):
    visited[start] = True
    global count
    count += 1
    for next_node in graph[start]:
        if next_node == end:
            break
        if not visited[next_node]:
            dfs(next_node, end)
            visited[next_node] = True

dfs(start, end)
print(count)