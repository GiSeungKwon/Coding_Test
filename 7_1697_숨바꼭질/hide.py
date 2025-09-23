from collections import deque

MAX = 100001
n, k = map(int, input().split())
graph = [-1] * MAX
visited = [False] * MAX

def bfs():
    queue = deque()
    queue.append(n)
    visited[n] = True
    graph[n] = 0

    while queue:
        now = queue.popleft()
        if now == k:
            return graph[now]

        for next_node in (now + 1, now - 1, 2 * now):
            if 0 <= next_node < MAX and not visited[next_node]:
                visited[next_node] = True
                graph[next_node] = graph[now] + 1
                queue.append(next_node)
    return -1

result = bfs()
if result == -1:
    print("못 잡음")
else:
    print(result)