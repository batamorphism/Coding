# 格子点の候補は、(1, 2)を足したり引いたりしたもの
def main():
    x0, y0, x1, y1 = map(int, input().split())

    points_0 = set()
    points_1 = set()
    dx_list = [1, -1]
    dy_list = [2, -2]
    for dx in dx_list:
        for dy in dy_list:
            points_0.add((x0+dx, y0+dy))
            points_1.add((x1+dx, y1+dy))
    dx_list = [2, -2]
    dy_list = [1, -1]
    for dx in dx_list:
        for dy in dy_list:
            points_0.add((x0+dx, y0+dy))
            points_1.add((x1+dx, y1+dy))

    # point_0とpoint_1で共通部分があるか
    point = points_0 & points_1
    if point:
        print('Yes')
    else:
        print('No')


main()
