n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    print(graph[i])