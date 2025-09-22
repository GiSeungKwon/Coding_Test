from collections import deque

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

def bfs(start, end):
    count = 0
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        count += 1
        # print(now, end=' ')
        for next_node in graph[now]:
            if next_node == end:
                return count
            else:
                queue.append(next_node)
count = bfs(start, end)
print(count)