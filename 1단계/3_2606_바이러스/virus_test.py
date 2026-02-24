from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
print(f"graph: {graph}")
visited = [False] * (n+1)
print(f"visited: {visited}")

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
print(f"graph: {graph}")

queue = deque()
queue.append(1)
visited[1] = True
while queue:
    now = queue.popleft()
    for next_node in graph[now]:
        if not visited[next_node]:
            visited[next_node] = True
            queue.append(next_node)
print(visited)
count = 0
for vi in visited:
    if vi == True:
        count += 1
print(count - 1)