import sys
from functools import lru_cache
from itertools import product
sys.setrecursionlimit(10**6)
# ミニマックス法
# score(r, c) -> (r, c), (r_end-1, c_end-1)からなるゲームで、r, cにおける最大値
# Takahashi君はscoreを最大化しようとする
# Aoki君はscoreを最小化しようとする


def main():
    r_end, c_end = map(int, input().split())
    grid = [input() for _ in range(r_end)]
    INF = float('inf')

    def calc_val(r, c):
        if grid[r][c] == '+':
            return 1
        else:
            return -1

    """
    @lru_cache(None)
    def score(r, c):
        if r == r_end-1 and c == c_end-1:
            return 0
        if (r+c) % 2 == 0:
            # TakaのTurn
            # 最大化しようとする
            ret = -INF
            if r+1 < r_end:
                val = calc_val(r+1, c)
                ret = max(ret, score(r+1, c) + val)
            if c+1 < c_end:
                val = calc_val(r, c+1)
                ret = max(ret, score(r, c+1) + val)
        else:
            # AokiのTurn
            # 最小化しようとする
            ret = INF
            if r+1 < r_end:
                val = calc_val(r+1, c)
                ret = min(ret, score(r+1, c) - val)
            if c+1 < c_end:
                val = calc_val(r, c+1)
                ret = min(ret, score(r, c+1) - val)
        return ret
    """
    score = [[0]*c_end for _ in range(r_end)]
    for r, c in product(range(r_end-1, -1, -1), range(c_end-1, -1, -1)):
        if r == r_end-1 and c == c_end-1:
            score[r][c] = 0
            continue
        if (r+c) % 2 == 0:
            # TakaのTurn
            # 最大化しようとする
            ret = -INF
            if r+1 < r_end:
                val = calc_val(r+1, c)
                ret = max(ret, score[r+1][c] + val)
            if c+1 < c_end:
                val = calc_val(r, c+1)
                ret = max(ret, score[r][c+1] + val)
        else:
            # AokiのTurn
            # 最小化しようとする
            ret = INF
            if r+1 < r_end:
                val = calc_val(r+1, c)
                ret = min(ret, score[r+1][c] - val)
            if c+1 < c_end:
                val = calc_val(r, c+1)
                ret = min(ret, score[r][c+1] - val)
        score[r][c] = ret

    start_score = score[0][0]
    if start_score > 0:
        print('Takahashi')
    elif start_score < 0:
        print('Aoki')
    else:
        print('Draw')


main()
