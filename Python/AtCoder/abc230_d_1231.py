# 区間スケジューリング
def main():
    n, d = map(int, input().split())
    wall_list = [tuple(map(int, input().split())) for _ in range(n)]
    wall_list.sort(key=lambda x: x[1])

    INF = float('inf')
    punch_x = -INF
    cnt = 0
    for le, ri in wall_list:
        # punch_x + d - 1まで破壊されるため
        # le <= punch_x + d - 1 ならば破壊される
        destroy = (le <= punch_x + d - 1)
        if destroy:
            continue
        cnt += 1
        punch_x = ri

    print(cnt)


main()
