# 平行移動は、一番左上にある頂点で判定できる
# 頂点からなる集合を考える
# 回転は、x, y -> -y, x で計算できる
def main():
    n = int(input())
    # 回転しないほうはsetで持つ
    point_set_1 = set()
    point_set_2 = set()
    for r in range(n):
        row = input()
        for c, val in enumerate(row):
            if val == '#':
                point_set_1.add((r, c))

    for r in range(n):
        row = input()
        for c, val in enumerate(row):
            if val == '#':
                point_set_2.add((r, c))

    if len(point_set_1) != len(point_set_2):
        print('No')
        return

    base_point_1 = sorted(list(point_set_1))[0]
    for _ in range(4):
        point_set_2 = rotate(point_set_2, base_point_1)
        if point_set_1 == point_set_2:
            print('Yes')
            return
        # show_point_set(point_set_2, n)
    print('No')


def show_point_set(point_set, n):
    ret = [['.']*n for _ in range(n)]
    for r, c in point_set:
        if r < 0 or r >= n or c < 0 or c >= n:
            continue
        ret[r][c] = '#'
    for row in ret:
        print(''.join(row))


def rotate(point_list, base_point_1):
    new_point_list = []
    for r, c in point_list:
        new_point_list.append((-c, r))
    new_point_list.sort()
    base_point_2 = new_point_list[0]
    diff = (base_point_1[0] - base_point_2[0], base_point_1[1] - base_point_2[1])
    new_point_set = set()
    for pre_r, pre_c in new_point_list:
        cur_r = pre_r + diff[0]
        cur_c = pre_c + diff[1]
        new_point_set.add((cur_r, cur_c))
    return new_point_set


main()
