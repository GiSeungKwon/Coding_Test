from collections import deque

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

t = int(input())
for _ in range(t):
    n = int(input())
    locations = [tuple(map(int, input().split())) for _ in range(n+2)]
    # 0: 집, 1~n: 편의점, n+1: 페스티벌

    visited = [False] * (n+2)

    def bfs():
        queue = deque([0])  # 집에서 출발
        visited[0] = True
        while queue:
            now = queue.popleft()
            if now == n+1:  # 페스티벌 도착
                return True
            for nxt in range(n+2):
                if not visited[nxt] and manhattan(locations[now], locations[nxt]) <= 1000:
                    visited[nxt] = True
                    queue.append(nxt)
        return False

    print("happy" if bfs() else "sad")