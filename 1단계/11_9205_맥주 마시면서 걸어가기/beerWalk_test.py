test_case = int(input())
print(f"test_case: {test_case}")
convenience_n = int(input())
print(f"convenience_n: {convenience_n}")
start_coordinate = map(int, input().split())

convenience_coordinate = [list(map(int, input().split())) for _ in range(convenience_n)]
end_coordinate = [list(map(int, input().split()))]
print()