from collections import deque

f, s, g, u, d = map(int, input().split())

queue = deque()
queue.append((s, 0))
visited = [False] * (f+1)

while queue:
    now, count = queue.popleft()
    for next_node in (now + u, now - d):
        if 0 <= next_node <= 1000001 and :
