# 미생물 연구 문제 풀이 (시뮬레이션)
# N <= 15, Q <= 50 이므로 완전탐색(브루트포스)로 충분

from collections import deque

def in_bounds(x, y, N):
    return 0 <= x < N and 0 <= y < N

def cells_in_rect(r1, c1, r2, c2):
    # 입력이 (r1, c1, r2, c2), 칸은 x=r1..r2-1, y=c1..c2-1
    cells = []
    for x in range(r1, r2):
        for y in range(c1, c2):
            cells.append((x, y))
    return cells

def bfs_count_and_collect(start, grid, N, id_):
    # grid: grid[y][x], id_는 찾고자 하는 id
    sx, sy = start
    q = deque([(sx, sy)])
    visited = set([(sx, sy)])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited and grid[ny][nx] == id_:
                visited.add((nx, ny))
                q.append((nx, ny))
    return visited

def simulate_one(N, grid, insertion_time, next_id, rect):
    """
    grid: current grid (list of lists) with 0 for empty or id>0
    insertion_time: dict id -> insertion index for tie-break
    next_id: integer id to use for new microbe
    rect: tuple (r1,c1,r2,c2)
    returns: (result_score, next_id) and grid is modified in-place (after removal and placement steps)
    """
    r1, c1, r2, c2 = rect

    # 1) 겹치는 id 집합 수집 (덮어쓰기 전)
    overlapped_ids = set()
    for x in range(r1, r2):
        for y in range(c1, c2):
            v = grid[y][x]
            if v != 0:
                overlapped_ids.add(v)

    # 2) 새 id로 덮어쓰기
    new_id = next_id
    insertion_time[new_id] = next_id  # 투입 순서(작을수록 먼저)
    for x in range(r1, r2):
        for y in range(c1, c2):
            grid[y][x] = new_id

    # 3) overlapped_ids 각각에 대해 남아있는 칸이 여러 컴포넌트로 나뉘면 전부 소멸
    for oid in list(overlapped_ids):
        # 남아있는 좌표 수
        remaining = [(x, y) for y in range(N) for x in range(N) if grid[y][x] == oid]
        if len(remaining) == 0:
            continue
        # BFS로 연결성 검사
        comp = bfs_count_and_collect(remaining[0], grid, N, oid)
        if len(comp) != len(remaining):
            # 여러 조각으로 쪼개졌으므로 전부 소멸
            for (x, y) in remaining:
                grid[y][x] = 0

    # 4) 새 배양 용기로 옮김
    # 남아있는 id 목록과 그 좌표 집합 구하기
    ids_present = {}
    for y in range(N):
        for x in range(N):
            v = grid[y][x]
            if v != 0:
                ids_present.setdefault(v, []).append((x, y))

    # 새 격자 (빈칸)
    new_grid = [[0]*N for _ in range(N)]
    placed_ids = set()

    # 반복: 영역이 가장 큰 것부터 (tie -> insertion_time 작은 것) 처리
    while ids_present:
        # 선택
        # compute area and tie-break by insertion_time (smaller = earlier)
        best_id = None
        best_area = -1
        best_time = 10**9
        for id_, cells in ids_present.items():
            area = len(cells)
            t = insertion_time.get(id_, 10**9)
            if area > best_area or (area == best_area and t < best_time):
                best_area = area
                best_time = t
                best_id = id_

        shape = ids_present.pop(best_id)  # 이 미생물의 셀 좌표들
        # normalize shape relative to its min x,min y (we must preserve shape)
        xs = [p[0] for p in shape]
        ys = [p[1] for p in shape]
        minx, maxx = min(xs), max(xs)
        miny, maxy = min(ys), max(ys)
        norm = [(x - minx, y - miny) for (x,y) in shape]
        width = maxx - minx + 1
        height = maxy - miny + 1

        # try placements: ox from 0..N-width, oy from 0..N-height,
        # tie-break: minimal x then minimal y
        placed = False
        for ox in range(0, N - width + 1):
            if placed:
                break
            for oy in range(0, N - height + 1):
                # check each normalized cell mapped to (ox+nx, oy+ny)
                ok = True
                for nx, ny in norm:
                    tx, ty = ox + nx, oy + ny
                    if new_grid[ty][tx] != 0:
                        ok = False
                        break
                if ok:
                    # place with the original id (or we could use new indices)
                    for nx, ny in norm:
                        tx, ty = ox + nx, oy + ny
                        new_grid[ty][tx] = best_id
                    placed = True
                    placed_ids.add(best_id)
                    break

        # if not placed -> this microbe disappears (do nothing)

    # 5) 결과 계산: 인접 쌍 찾기 (각 쌍 한번만)
    # compute areas in new_grid
    areas = {}
    for y in range(N):
        for x in range(N):
            v = new_grid[y][x]
            if v != 0:
                areas[v] = areas.get(v, 0) + 1

    pairs = set()
    dirs = [(1,0),(0,1)]
    for y in range(N):
        for x in range(N):
            v = new_grid[y][x]
            if v == 0:
                continue
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    u = new_grid[ny][nx]
                    if u != 0 and u != v:
                        a, b = (v, u) if v < u else (u, v)
                        pairs.add((a,b))
    score = 0
    for a,b in pairs:
        score += areas.get(a,0) * areas.get(b,0)

    # replace original grid with new_grid (새 용기가 기록된 최종 상태)
    # Problem statement records experiment AFTER moving, so we set current grid = new_grid
    for y in range(N):
        for x in range(N):
            grid[y][x] = new_grid[y][x]

    return score, next_id + 1

# main
def main():
    import sys
    sys.stdin = open("./3단계/2025_상반기_오후1번_MicrobiologyResearch/input.txt", "r")

    N, Q = map(int, input().split()) # N: 용기 크기 / Q: 실험 횟수
    rects = [tuple(map(int, input().split())) for _ in range(Q)]

    print(N, Q)
    print(rects)
    # initial empty grid
    grid = [[0]*N for _ in range(N)]
    insertion_time = {}  # id -> insertion order (use id itself)
    next_id = 1

    for i in range(Q):
        score, next_id = simulate_one(N, grid, insertion_time, next_id, rects[i])
        print(score)

if __name__ == "__main__":
    main()
