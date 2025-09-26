from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, grid, N, id_):
    """같은 id_를 가진 연결된 영역을 BFS로 탐색"""
    q = deque([start])
    visited = {start}
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited and grid[ny][nx] == id_:
                visited.add((nx, ny))
                q.append((nx, ny))
    return visited

def simulate(N, grid, insertion_time, next_id, rect):
    r1, c1, r2, c2 = rect

    # 새 사각형이 겹치는 기존 미생물 id 집합
    overlapped = {grid[y][x] for x in range(r1, r2) for y in range(c1, c2) if grid[y][x]}

    # 새로운 미생물 ID 부여
    new_id = next_id
    insertion_time[new_id] = next_id
    for x in range(r1, r2):
        for y in range(c1, c2):
            grid[y][x] = new_id

    # 겹친 미생물 중 분리된 경우 소멸 처리
    for oid in overlapped:
        remain = [(x, y) for y in range(N) for x in range(N) if grid[y][x] == oid]
        if remain and len(bfs(remain[0], grid, N, oid)) != len(remain):
            for x, y in remain:
                grid[y][x] = 0

    # 새 용기 준비
    new_grid = [[0] * N for _ in range(N)]
    ids = {}
    for y in range(N):
        for x in range(N):
            if grid[y][x]:
                ids.setdefault(grid[y][x], []).append((x, y))

    while ids:
        # 가장 큰 영역 (tie → 먼저 투입된 것 우선)
        best = max(ids, key=lambda k: (len(ids[k]), -insertion_time[k]))
        shape = ids.pop(best)
        xs, ys = zip(*shape)
        norm = [(x - min(xs), y - min(ys)) for x, y in shape]
        w, h = max(xs) - min(xs) + 1, max(ys) - min(ys) + 1

        placed = False
        for ox in range(N - w + 1):
            if placed:
                break
            for oy in range(N - h + 1):
                if all(new_grid[oy + ny][ox + nx] == 0 for nx, ny in norm):
                    for nx, ny in norm:
                        new_grid[oy + ny][ox + nx] = best
                    placed = True
                    break

    # 점수 계산
    areas, pairs = {}, set()
    for y in range(N):
        for x in range(N):
            v = new_grid[y][x]
            if v:
                areas[v] = areas.get(v, 0) + 1
            for dx, dy in [(1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    u = new_grid[ny][nx]
                    if v and u and v != u:
                        pairs.add(tuple(sorted((v, u))))

    score = sum(areas[a] * areas[b] for a, b in pairs)

    # 새 grid로 교체
    for y in range(N):
        grid[y] = new_grid[y][:]

    return score, next_id + 1

def main():
    import sys
    sys.stdin = open("./3단계/2025_상반기_오후1번_MicrobiologyResearch/input.txt")
    N, Q = map(int, input().split())
    rects = [tuple(map(int, input().split())) for _ in range(Q)]

    grid = [[0] * N for _ in range(N)]
    insertion_time = {}
    next_id = 1

    for rect in rects:
        score, next_id = simulate(N, grid, insertion_time, next_id, rect)
        print(score)

if __name__ == "__main__":
    main()