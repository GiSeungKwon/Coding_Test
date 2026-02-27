from collections import deque
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


    print()
