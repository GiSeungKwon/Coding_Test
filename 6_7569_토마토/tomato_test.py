from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

count = [0] * (n+1)
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(n):
    graph[i].sort()
print(graph)

def bfs(v):
    visited[v] = True
    queue = deque()
    queue.append(v)
    while queue:
        now = queue.popleft()
        print(now, end = ' ')
        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                count[next_node] = count[now] + 1
                queue.append(next_node)

bfs(a)
print(count[b])