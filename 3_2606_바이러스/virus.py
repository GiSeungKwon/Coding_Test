def dfs(v, visited, graph):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited, graph)

# 입력 받기
n = int(input())  # 컴퓨터 수
m = int(input())  # 연결 쌍 수

# 인접 리스트 생성
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 실행 (1번 컴퓨터부터 시작)
dfs(1, visited, graph)

# 결과 출력 (1번 컴퓨터 제외한 감염된 컴퓨터 수)
print(visited.count(True) - 1)
