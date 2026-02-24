from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
for i in range(n):
    print(graph[i])

visited = [[False] * n for _ in range(n)]
# for i in range(n):
#     print(visited[i])

dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]

result = []
danji_count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            danji_count += 1
            queue = deque()
            count = 0
            queue.append((i, j))
            print()
            print(f"queue.append((i:{i}, j:{j}))")
            while queue:
                y, x = queue.popleft()
                print(f"queue.popleft() y:{y}, x:{x}, count:{count}")
                for k in range(4):
                    ny, nx = y+dy[k], x+dx[k]
                    if 0<=ny<n and 0<=nx<n and graph[ny][nx]==1 :
                        if not visited[ny][nx]:
                            count += 1
                            visited[ny][nx] = True
                            queue.append((ny, nx))
                            print(f"queue: {queue}")
                            for i in range(n):
                                print(f"{visited[i]}")
            result.append(count)

print(f"result: {sorted(result)}")
# 출력
# 단지수
# 각 단지 수를 오름차순