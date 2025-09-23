from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [False] * (f+1)
graph = [-1] * (f+1)

def bfs(start, end):
    visited[start] = True
    queue = deque()
    queue.append(start)
    graph[start] = 0

    while queue:
        now = queue.popleft()
        if now == end:
            return graph[now]
        for next_node in (now+u, now-d):
            if 0<=next_node<=f and not visited[next_node]:
                visited[next_node] = True
                graph[next_node] = graph[now] + 1
                queue.append(next_node)
    return -1

result = bfs(s, g)
if result == -1:
    print("use the stairs")
else:
    print(result)
