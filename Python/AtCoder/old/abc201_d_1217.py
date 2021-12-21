from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)
# ミニマックス法


def main():
    INF = 4000+100
    # r_end, c_end = map(int, input().split())
    # grid = [list(input()) for _ in range(r_end)]
    r_end, c_end = 800, 800
    grid = ['+'*c_end for _ in range(r_end)]

    # DP[r][c] = コマがr, cにあるときの、TakaScore-AokiScoreの最適値

    @lru_cache(maxsize=None)
    def score_of(r, c):
        if r == r_end-1 and c == c_end-1:
            return 0
        if (r+c) % 2 == 0:
            # 最大化する
            ret = -INF
            # 横に動くとき
            if c+1 < c_end:
                if grid[r][c+1] == '+':
                    val = 1
                else:
                    val = -1
                ret = max(ret, score_of(r, c+1) + val)
            # 縦に動くとき
            if r+1 < r_end:
                if grid[r+1][c] == '+':
                    val = 1
                else:
                    val = -1
                ret = max(ret, score_of(r+1, c) + val)
        else:
            # 最小化する
            ret = INF
            # 横に動くとき
            if c+1 < c_end:
                if grid[r][c+1] == '+':
                    val = 1
                else:
                    val = -1
                ret = min(ret, score_of(r, c+1) - val)
            # 縦に動くとき
            if r+1 < r_end:
                if grid[r+1][c] == '+':
                    val = 1
                else:
                    val = -1
                ret = min(ret, score_of(r+1, c) - val)
        return ret

    ans = score_of(0, 0)

    if ans > 0:
        print('Takahashi')
    elif ans == 0:
        print('Draw')
    else:
        print('Aoki')


main()
