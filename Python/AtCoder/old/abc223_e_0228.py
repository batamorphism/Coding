from itertools import permutations


# 3つの長方形を置いた場合
# 少なくとも一つのx軸かy軸に平行な直線が存在し
# 片方に長方形が1つしかない状態にできる
def main():
    x0, y0, a0, b0, c0 = map(int, input().split())

    for x, y in permutations([x0, y0]):
        for a, b, c in permutations([a0, b0, c0]):
            if solve(x, y, a, b, c):
                print('Yes')
                return
    print('No')


def solve(x, y, a, b, c):
    # 題意を満たす条件を、ある1通りの組み合わせに対してのみ行う
    # x軸と平行な直線で分ける
    # 分けられるのは、長方形aとする
    a_w = x
    a_h = (a + a_w - 1) // a_w  # 切り上げ
    y -= a_h
    if y <= 0:
        return False
    ret = False
    for x_, y_ in permutations([x, y]):
        if solve1(x_, y_, b, c):
            ret = True
    return ret


def solve1(x, y, b, c):
    b_w = x
    b_h = (b + b_w - 1) // b_w  # 切り上げ
    y -= b_h
    if y <= 0:
        return False
    if c > x*y:
        return False
    return True


main()
