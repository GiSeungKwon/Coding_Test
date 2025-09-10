from collections import deque

m, n, h = map(int, input().split())

graph = [[[0] * m for _ in range(n)] for _ in range(h)]
for h_ in range(h):
    for n_ in range(n):
        graph[h_][n_] = list(map(int, input().split()))

dh = [-1, 1, 0, 0, 0, 0]
dn = [0, 0, -1, 1, 0, 0]
dm = [0, 0, 0, 0, -1, 1]

queue = deque()
for h_ in range(h):
    for n_ in range(n):
        for m_ in range(m):
            if graph[h_][n_][m_] == 1:
                queue.append((h_, n_, m_))

while queue:
    h_, n_, m_ = queue.popleft()
    for i in range(6):
        nh = h_ + dh[i]
        nn = n_ + dn[i]
        nm = m_ + dm[i]
        if 0<=nh<h and 0<=nn<n and 0<=nm<m and graph[nh][nn][nm] == 0:
            graph[nh][nn][nm] = graph[h_][n_][m_] + 1
            queue.append((nh, nn, nm))

days = 0
for h_ in range(h):
    for n_ in range(n):
        for m_ in range(m):
            days = max(days, graph[h_][n_][m_])

print(days-1)