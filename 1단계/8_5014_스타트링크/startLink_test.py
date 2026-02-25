from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [False] * (f+1)

def solution(f, s, g, u, d, visited):
    queue = deque()
    queue.append((s, 0))
    visited[s] = True

    while queue:
        now, count = queue.popleft()
        if now == g:
            return count
        for next_node in (now + u, now - d):
            if 0 <= next_node <= f and not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, count + 1))
    return "use the stairs"

print(solution(f, s, g, u, d, visited))