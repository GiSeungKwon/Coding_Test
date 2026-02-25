from collections import deque

n, k = map(int, input().split())
max = 1000001
graph = [[-1] for _ in range(max)]
visited = [False] * max

queue = deque()
queue.append((n, 0))
visited[n] = True

while queue:
    print(f"queue: {queue}")
    now, count = queue.popleft()
    if now == k:
        print(count)
        break
    for next_node in (now+1, now-1, now*2):
        if 0<=next_node<max and not visited[next_node]:
            visited[next_node] = True
            queue.append((next_node, count + 1))