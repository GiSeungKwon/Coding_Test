from collections import deque

n = int(input())
start, end = map(int, input().split())
m = int(input())
visited = [False]*(n+1)
distance = [-1]*(n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()

print(n)
print(start, end)
print(m)
print(visited)
print(distance)

def bfs(start):
    distance[start] = 0
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                distance[next_node] = distance[now]+1
                queue.append(next_node)
bfs(start)
print(distance[end])