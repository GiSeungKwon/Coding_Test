from collections import deque

test_case = int(input())
print(f"test_case: {test_case}")
convenience_n = int(input())
print(f"convenience_n: {convenience_n}")
start_coordinate = list(map(int, input().split()))
print(f"start_coordinate: {start_coordinate}")
convenience_coordinate = [list(map(int, input().split())) for _ in range(convenience_n)]
print(f"convenience_coordinate: {convenience_coordinate}")
end_coordinate = list(map(int, input().split()))
print(f"end_coordinate: {end_coordinate}")

def manhattan(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

visited = [False] * convenience_n
queue = deque()
queue.append(start_coordinate)

while queue:
    y, x = queue.popleft()
