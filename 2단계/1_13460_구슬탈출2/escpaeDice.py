from collections import deque


def move(y, x, dy, dx, board):
    cnt = 0
    # 벽(#)을 만나거나 구멍(O)에 들어가기 전까지 계속 이동
    while board[y + dy][x + dx] != '#' and board[y][x] != 'O':
        y += dy
        x += dx
        cnt += 1
    return y, x, cnt


def bfs(board, N, M, red, blue):
    # 방문 여부: visited[red_y][red_x][blue_y][blue_x]
    visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((*red, *blue, 0))  # (ry, rx, by, bx, depth)
    visited[red[0]][red[1]][blue[0]][blue[1]] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우

    while q:
        ry, rx, by, bx, depth = q.popleft()
        if depth >= 10:
            break
        for dy, dx in directions:
            nry, nrx, rc = move(ry, rx, dy, dx, board)
            nby, nbx, bc = move(by, bx, dy, dx, board)

            # 파란 구슬이 구멍에 들어가면 실패
            if board[nby][nbx] == 'O':
                continue
            # 빨간 구슬이 구멍에 들어가면 성공
            if board[nry][nrx] == 'O':
                return depth + 1

            # 두 구슬이 같은 칸에 도착하면 → 이동 거리 큰 쪽을 한 칸 뒤로
            if nry == nby and nrx == nbx:
                if rc > bc:
                    nry -= dy
                    nrx -= dx
                else:
                    nby -= dy
                    nbx -= dx

            # 방문하지 않은 상태라면 큐에 추가
            if not visited[nry][nrx][nby][nbx]:
                visited[nry][nrx][nby][nbx] = True
                q.append((nry, nrx, nby, nbx, depth + 1))
    return -1

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().strip())) for _ in range(N)]
    red = blue = None

    for i in range(N):
        for j in range(M):
            if graoh[i][j] == 'R':
                red = (i, j)
                graoh[i][j] = '.'  # 빈칸 처리
            elif graoh[i][j] == 'B':
                blue = (i, j)
                board[i][j] = '.'

    print(bfs(board, N, M, red, blue))
