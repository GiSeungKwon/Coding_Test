from collections import deque

n = int(input())
start, end = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [-1] * (n+1)  # 촌수 기록 (-1 = 아직 방문 안 함)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    distance[start] = 0  # 자기 자신은 0촌
    while queue:
        now = queue.popleft()
        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                distance[next_node] = distance[now] + 1
                queue.append(next_node)

bfs(start)
print(distance[end])