from collections import deque

# input 처리 - coordinate 정의가 x, y가 아니므로 y, x로 정의해서 문제 접근
test_case = int(input())
for t in range(test_case):
    convenience_store_n = int(input())
    home_coordinate = list(map(int, input().split()))
    convenience_store_coordinates = [list(map(int, input().split())) for _ in range(convenience_store_n)]
    destination_coordinate = list(map(int, input().split()))
    beer_n = 20
    visited = [[False] * (destination_coordinate[1]+1) for _ in range(destination_coordinate[0]+1)]
    queue = deque()
    dy, dx = [1, -1, 0, 0], [0, 0, -1, 1] # 상하좌우
    queue.append((home_coordinate[0], home_coordinate[1], 0))
    flag = False
    while queue:
        y, x, move = queue.popleft() # y, x, 움직인 거리
        # 목적지 도착
        if y == destination_coordinate[0] and x == destination_coordinate[1] and move <= 1000:
            print(f"y:{y} == destination_coordinate[0]:{destination_coordinate[0]}")
            print(f"x:{x} == destination_coordinate[1]:{destination_coordinate[1]}")
            print(f"목적지 도착 flag = True")
            flag = True
            break
        # 편의점 도착
        for convenience_store_coordinate in convenience_store_coordinates:
            if y == convenience_store_coordinate[0] and x == convenience_store_coordinates[1] and move <= 1000:
                print(f"y:{y} == convenience_store_coordinate[0]:{convenience_store_coordinate[0]}")
                print(f"x:{x} == convenience_store_coordinates[1]:{convenience_store_coordinates[1]}")
                print(f"편의점 도착 move = {move} -> 0")
                move = 0
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if home_coordinate[0] <= ny <= destination_coordinate[0] and home_coordinate[1] <= nx <= destination_coordinate[1]:
                if not visited[ny][nx] and move <= 1000:
                    visited[ny][nx] = True
                    queue.append((ny, nx, move+1))
    if flag:
        print("happy")
    else:
        print("sad")