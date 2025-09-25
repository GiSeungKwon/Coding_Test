from collections import deque

F, S, G, U, D = map(int, input().split())
graph = [-1] * (F+1)
visited = [False] * (F+1)

def bfs():
    queue = deque()
    queue.append(S)
    visited[S] = True
    graph[S] = 0
    while queue:
        now = queue.popleft()
        if now == G:
            return graph[now]

        for next_node in (now-D, now+U):
            if 1<=next_node<=F and not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                graph[next_node] = graph[now] + 1
    return -1

result = bfs()
if result == -1:
    print("use the stairs")
else:
    print(result)