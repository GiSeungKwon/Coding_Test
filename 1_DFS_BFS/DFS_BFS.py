from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(n+1):
    graph[i].sort()
print(graph)

def dfs(v, visit):
    visit[v] = True
    print(v, end = ' ')
    for nnode in graph[v]:
        if not visit[nnode]:
            visit[nnode] = True
            dfs(nnode, visit)

def bfs(v, visit):
    queue = deque()
    queue.append(v)
    visit[v] = True
    while queue:
        now = queue.popleft()
        print(now, end = ' ')
        for nnode in graph[now]:
            if not visit[nnode]:
                visit[nnode] = True
                queue.append(nnode)

visit_dfs = [False] * (n+1)
dfs(v, visit_dfs)
print()
visit_bfs = [False] * (n+1)
bfs(v, visit_bfs)