from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def solution(a, b, graph, visited):
    queue = deque()
    queue.append((a, 0))
    visited[a] = True

    while queue:
        now, count = queue.popleft()
        if now == b:
            return count
        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, count + 1))
    return -1

print(solution(a, b, graph, visited))