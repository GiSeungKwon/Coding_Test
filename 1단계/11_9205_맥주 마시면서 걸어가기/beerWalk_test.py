from collections import deque

def manhattan(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

test_case = int(input())
for _ in range(test_case):
    # convenience_n: 2
    convenience_n = int(input())
    # start_coord: [0, 0]
    start_coord = list(map(int, input().split()))
    # convenience_coord: [[1000, 0], [1000, 1000]]
    convenience_coord = [list(map(int, input().split())) for _ in range(convenience_n)]
    # end_coord: [2000, 1000]
    end_coord = list(map(int, input().split()))

    visited = [False] * convenience_n
    queue = deque()
    queue.append(start_coord)
    flag = False
    while queue:
        y, x = queue.popleft()
        if manhattan([y, x], end_coord) <= 1000:
            flag = True
            break
        for i in range(convenience_n):
            if manhattan([y, x], convenience_coord[i]) <= 1000 and not visited[i]:
                visited[i] = True
                queue.append(convenience_coord[i])
    if flag:
        print("happy")
    else:
        print("sad")