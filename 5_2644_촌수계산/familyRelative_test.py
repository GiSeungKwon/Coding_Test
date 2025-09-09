from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
print(f"n:{n} a:{a} b:{b} m:{m}")

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(n+1):
    graph[i].sort()

visited = [False] * (n+1)
count = [0] * (n+1)

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        now = queue.popleft()
        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                count[next_node] = count[now] + 1
                queue.append(next_node)
bfs(a)
print(count[b])