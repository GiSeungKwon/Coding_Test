from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
for i in range(n+1):
    graph[i].sort()
print(graph)

def bfs(start, end):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        global count
        now = queue.popleft()
        print(now, end=' ')
        for next_node in graph[now]:
            if not visited[next_node]:
                if next_node == end:
                    break
                count += 1
                visited[next_node] = True
                queue.append(next_node)

bfs(a, b)
print(count)