from collections import deque

n, m, v = map(int, input().split())
print(n, m, v)

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)

