from collections import deque

n = int(input())
start, end = map(int, input().split())
m = int(input())

visited = [False] * (n+1)
print(visited)
distance = [-1] * (n+1)
print(distance)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()
print(graph)

def bfs():
    queue = deque()
    queue.append(start)
    visited[start] = True
    distance[start] = 0
    while queue:
        now = queue.popleft()
        if now == end:
            return distance[now]
        for next_node in graph[now]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                distance[next_node] = distance[now] + 1
    return -1

print(bfs())