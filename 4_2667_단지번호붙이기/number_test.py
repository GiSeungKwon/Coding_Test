n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
print(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
