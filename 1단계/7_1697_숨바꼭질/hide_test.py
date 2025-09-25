from collections import deque

n, k = map(int, input().split())
graph = [-1] * (2*k)
visited = [False] * (2*k)

def bfs():
    queue = deque()
    queue.append(n)
    visited[n] = True
    graph[n] = 0

    while queue:
        now = queue.popleft()
        if now == k:
            return graph[now]
        for next_node in (now-1, now+1, now*2):
            if 0<=next_node<2*k and not visited[next_node]:
                visited[next_node] = True
                graph[next_node] = graph[now] + 1
                queue.append(next_node)
    return -1
print(bfs())