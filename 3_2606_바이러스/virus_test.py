from collections import deque

n = int(input())
m = int(input())
print(f"n: {n}, m: {m}")

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
for i in range(n+1):
    graph[i].sort()
print(graph)

def dfs(v, visited):
    visited[v] = True

visited = [False] * (n+1)
dfs(1, visited)
