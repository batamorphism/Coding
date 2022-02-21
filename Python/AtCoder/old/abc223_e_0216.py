from itertools import permutations


def main():
    x, y, a, b, c = map(int, input().split())

    for perm in permutations([a, b, c]):
        for is_x in range(2):
            # perm[0]と、perm[1]+perm[2]を分ける直線Lを考える
            # Lは、高さperm[0]/xを切り上げたものとなる
            if is_x:
                # 直線Lがx軸と平行の場合
                w = (perm[0] + y - 1) // y
                cur_x, cur_y = x-w, y
            else:
                h = (perm[0] + x - 1) // x  # 切り上げ
                cur_x, cur_y = x, y - h

            if cur_x == 0 or cur_y == 0:
                continue

            for is_x2 in range(2):
                # perm[1]と、perm[2]を分ける直線Lを考える
                if is_x2:
                    w = (perm[1] + cur_y - 1) // cur_y
                    nex_x, nex_y = cur_x-w, cur_y
                else:
                    h = (perm[1] + cur_x - 1) // cur_x  # 切り上げ
                    nex_x, nex_y = cur_x, cur_y - h
                # この段階で、perm[2]が収まるか
                if perm[2] <= nex_x*nex_y:
                    print('Yes')
                    return
    print('No')


main()
