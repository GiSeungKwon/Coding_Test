from collections import deque

def manhattan(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

t = int(input())

for _ in range(t):
    n = int(input())
    graph = [tuple(map(int, input().split())) for _ in range(n+2)]
    visited = [False] * (n+2)

    def bfs():
        visited[0] = True
        queue = deque()
        queue.append(0)
        while queue:
            now = queue.popleft()
            if now == n+1:
                return True
            for next_node in range(n+2):
                if not visited[next_node] and manhattan(graph[now], graph[next_node]) <= 1000:
                    visited[next_node] = True
                    queue.append(next_node)
        return False
    print("happy" if bfs() else "sad")