from collections import deque

def bfs(N, K):
    MAX = 100000
    visited = [False] * (MAX + 1)
    dist = [0] * (MAX + 1)

    queue = deque([N])
    visited[N] = True

    while queue:
        x = queue.popleft()
        if x == K:
            return dist[x]
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= MAX and not visited[nx]:
                visited[nx] = True
                dist[nx] = dist[x] + 1
                queue.append(nx)

# 입력
N, K = map(int, input().split())
print(bfs(N, K))
