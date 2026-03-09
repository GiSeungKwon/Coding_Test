from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
map = [list(input().strip()) for _ in range(n)]
simul_map = deepcopy(map)
for simul_i in range(n):
    print(simul_map[simul_i])
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
red, blue, hole = [], [], []
for i in range(n):
    for j in range(m):
        if map[i][j] == 'R':
            red = [i, j]
        elif map[i][j] == 'O':
            hole = [i, j]
        elif map[i][j] == 'B':
            blue = [i, j]

def move(r, c, dr, dc):
    count = 0
    while map[r+dr][c+dc] != '#':
        r += dr
        c += dc
        count += 1
        # 이동 중 구멍(O)을 만나면 즉시 멈춤!
        if map[r][c] == 'O':
            break
    return r, c, count

count = 0
queue = deque()
queue.append([red[0], red[1], blue[0], blue[1], count])

print(f"🚀 시뮬레이션 시작! 초기 상태: R{red}, B{blue}")
dir_names = ["(↑)", "(→)", "(↓)", "(←)"]
while queue:
    red_r, red_c, blue_r, blue_c, count = queue.popleft()
    if count >= 10:
        print("⚠️ 10번 시도 초과로 중단")
        print(-1)
        break
    for i in range(4):
        next_red_r, next_red_c, red_count = move(red_r, red_c, dr[i], dc[i])
        next_blue_r, next_blue_c, blue_count = move(blue_r, blue_c, dr[i], dc[i])
        print(f"[{count+1}회차] 방향: {dir_names[i]} 시도 중...")
        simul_map[red_r][red_c] = dir_names[i]
        simul_map[blue_r][blue_c] = dir_names[i]

        if map[next_blue_r][next_blue_c] == 'O':
            print(f"   ❌ 파란 구슬이 빠졌습니다. (B: {next_blue_r, next_blue_c})")
            continue
        if map[next_red_r][next_red_c] == 'O':
            print(f"🎉 성공! {count + 1}회차 만에 빨간 구슬 탈출 (방향: {dir_names[i]})")
            print(count+1)
            exit()
        if next_red_r == next_blue_r and next_red_c == next_blue_c:
            if red_count < blue_count:
                next_blue_r -= dr[i]
                next_blue_c -= dc[i]
                print(f"   ⚓ 파랑이 빨강 뒤로 보정됨: R{next_red_r, next_red_c}, B{next_blue_r, next_blue_c}")
            else:
                next_red_r -= dr[i]
                next_red_c -= dc[i]
                print(f"   ⚓ 빨강이 파랑 뒤로 보정됨: R{next_red_r, next_red_c}, B{next_blue_r, next_blue_c}")
        if not visited[next_red_r][next_red_c][next_blue_r][next_blue_c]:
            visited[next_red_r][next_red_c][next_blue_r][next_blue_c] = True
            queue.append([next_red_r, next_red_c, next_blue_r, next_blue_c, count+1])
            print(f"   ✅ 새로운 상태 큐 추가: R{next_red_r, next_red_c}, B{next_blue_r, next_blue_c}")
            simul_map[next_red_r][next_red_c] = "■"
            simul_map[next_blue_r][next_blue_c] = "■"

        for simul_i in range(n):
            print(simul_map[simul_i])
        print()
print(-1)