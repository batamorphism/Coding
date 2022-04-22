def main():
    n, q = map(int, input().split())
    point_list = []
    for _ in range(n):
        x, y = map(int, input().split())
        point_list.append((x, y))

    # (1, 0) -> (1, 1)
    # (0, 1) -> (1, -1)
    new_point_list = []
    for x, y in point_list:
        new_x = x + y
        new_y = x - y
        new_point_list.append((new_x, new_y))

    x_list = []
    y_list = []
    for x, y in new_point_list:
        x_list.append(x)
        y_list.append(y)
    x_max = max(x_list)
    x_min = min(x_list)
    y_max = max(y_list)
    y_min = min(y_list)

    ans_list = []
    for _ in range(q):
        i = int(input())
        i -= 1
        x, y = new_point_list[i]
        ans = -1
        ans = max(ans, x_max-x)
        ans = max(ans, x-x_min)
        ans = max(ans, y_max-y)
        ans = max(ans, y-y_min)
        ans_list.append(ans)

    print(*ans_list, sep='\n')


main()
