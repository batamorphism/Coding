from itertools import product
from functools import lru_cache
mod = 10**9 + 7


# 主客転倒
# 各マス毎に、ライトで照らされうるパターン数を求める
# これは、散らかってないマスの数をkとしたときに
# 2**k通りのうち、あるマス(r, c)が照らされるパターンがいくつあるか
# これは、照らされていないパターンを求めるのは容易なので、これから逆算する
def main():
    r_end, c_end = map(int, input().split())
    grid = [input() for _ in range(r_end)]

    # 横方向から照らされている数、縦方向から照らされている数
    row_cnt_of = [[0] * c_end for _ in range(r_end)]
    col_cnt_of = [[0] * c_end for _ in range(r_end)]
    for r, c in product(range(r_end), range(c_end)):
        if grid[r][c] == '.':
            row_cnt_of[r][c] = 1
            col_cnt_of[r][c] = 1

    # 累積和
    for r, c in product(range(r_end), range(c_end)):
        if grid[r][c] == '#':
            continue
        row_cnt_of[r][c] += row_cnt_of[r][c - 1] if c > 0 else 0
        col_cnt_of[r][c] += col_cnt_of[r-1][c] if r > 0 else 0

    # ライトで照らされるパターン数
    for r, c in product(range(r_end-1, -1, -1), range(c_end-1, -1, -1)):
        if grid[r][c] == '#':
            continue
        row_cnt_of[r][c] = max(row_cnt_of[r][c], row_cnt_of[r][c + 1] if c < c_end - 1 else 0)
        col_cnt_of[r][c] = max(col_cnt_of[r][c], col_cnt_of[r+1][c] if r < r_end - 1 else 0)

    # cnt_of[r][c] = (r, c)が照らされうるライトのマスの数
    cnt_of = [[0] * c_end for _ in range(r_end)]
    for r, c in product(range(r_end), range(c_end)):
        if grid[r][c] == '#':
            cnt_of[r][c] = 0
            continue
        cnt = row_cnt_of[r][c] + col_cnt_of[r][c] - 1
        cnt_of[r][c] = cnt

    """
    print(cnt_of)
    print(row_cnt_of)
    print(col_cnt_of)
    """

    k = 0
    # kは高々4000
    for r, c in product(range(r_end), range(c_end)):
        if grid[r][c] == '.':
            k += 1

    ans = 0
    ALL = modpow(2, k, mod)
    for r, c in product(range(r_end), range(c_end)):
        """
        cnt = cnt_of[r][c]
        not_light = pow(2, k-cnt, mod)
        light = ALL - not_light
        ans += light
        """
        ans += ALL - modpow(2, k-cnt_of[r][c], mod)
        ans %= mod
    print(ans)


@lru_cache(maxsize=None)
def modpow(a, n, mod):
    return pow(a, n, mod)


main()
