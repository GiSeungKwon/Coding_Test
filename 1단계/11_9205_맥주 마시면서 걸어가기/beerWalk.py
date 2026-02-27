from collections import deque

test_case = int(input())
print(f"test_case: {test_case}")
print()

def manhattan(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

for _ in range(test_case):
    convenience_n = int(input())
    print(f"convenience_n: {convenience_n}")
    start_coordinate = list(map(int, input().split()))
    print(f"start_coordinate: {start_coordinate}")
    convenience_coordinate_batch = [list(map(int, input().split())) for _ in range(convenience_n)]
    print(f"convenience_coordinate_batch: {convenience_coordinate_batch}")
    end_coordinate = list(map(int, input().split()))
    print(f"end_coordinate: {end_coordinate}")

    visited = [False] * convenience_n
    queue = deque()
    queue.append(start_coordinate)
    flag = False

    while queue:
        y, x = queue.popleft()
        if manhattan([y, x], end_coordinate) <= 1000:
            flag = True
            break
        for convenience_index in range(convenience_n):
            if manhattan([y, x], convenience_coordinate_batch[convenience_index]) <= 1000 and not visited[convenience_index]:
                visited[convenience_index] = True
                queue.append(convenience_coordinate_batch[convenience_index])

    if flag:
        print("happy")
    else:
        print("sad")
    print()