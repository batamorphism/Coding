import math


def main():
    h, w, k, v = map(int, input().split())
    # A[h][w]
    A = [list(map(int, input().split())) for _ in range(h)]
    # costは、マスに対応するAの総和+選択したマス数*k
    # v以下のcostで済ますことのできる、最大の面積を求めよ
    # 選択したマス数*kは固定なので、マスに対応するAの総和を最大化させる
    # v以下のcostで面積x以上の豪邸を立てることができるか
    # 左上と右下の点を指定すれば、計算できる。
    # B[c1][r1]-B[c0][r1]-B[c1][r0]+B[c0][r0]で、A[c0][r0]～A[c1-1][r1-1]の総和となるようにする
    # B[c][r]を、A[0][0]～A[c-1][r-1]の総和とする
    B = [[0]*(w+1) for _ in range(h+1)]
    for r in range(1, h+1):
        for c in range(1, w+1):
            B[r][c] = B[r-1][c]+B[r][c-1]-B[r-1][c-1]+A[r-1][c-1]

    ok = 0
    ng = h*w+1
    while ng-ok > 1:
        mid = (ok+ng)//2
        if check(B, h, w, k, v, mid):
            ok = mid
        else:
            ng = mid

    print(ok)


def check(B: list, h: int, w: int, k: int, v: int, area_size: int):
    is_ok = False
    for r_0 in range(h):
        for c_0 in range(w):
            for row in range(1, w+1):
                # 面積の縦幅
                col = math.ceil(area_size/row)
                r_1 = r_0+row-1
                c_1 = c_0+col-1
                if c_1 >= w or r_1 >= h:
                    continue
                cost = calc_cost(B, k, r_0, c_0, r_1, c_1)
                if cost <= v:
                    is_ok = True
                    return is_ok


def calc_cost(B: list, k: int, r0: int, c0: int, r1: int, c1: int) -> int:
    """
    c0r0, c1r1の範囲のコストを計算する
    """
    cost_1 = B[r1+1][c1+1]-B[r0][c1+1]-B[r1+1][c0]+B[r0][c0]
    cells_count = (r1-r0+1)*(c1-c0+1)
    cost_2 = cells_count*k
    return cost_1+cost_2


main()
