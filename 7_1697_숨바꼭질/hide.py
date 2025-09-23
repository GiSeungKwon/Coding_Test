from collections import deque

n, m = map(int, input().split())

max = 100000
visited = [False] * max
graph = [0] * max

def bfs(n, m):
    visited[n] = True
    queue = deque()
    queue.append(n)

    while queue:
        now = queue.popleft()
        if now == m:
            return graph[now]
        for next_node in (now-1, now+1, 2*now):
            if 0<=next_node<=max and not visited[next_node]:
                visited[next_node] = True
                graph[next_node] = graph[now] + 1
                queue.append(next_node)

print(bfs(n, m))