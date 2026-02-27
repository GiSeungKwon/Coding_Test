n, m = map(int, input().split())
print(f"n:{n}, m:{m}")
y, x, d = map(int, input().split())
print(f"y:{y}, x:{x}, d:{d}")
graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    print(graph[i])