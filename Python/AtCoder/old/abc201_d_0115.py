def main():
    r_end, c_end = map(int, input().split())
    INF = float('inf')
    A = [list(input()) for _ in range(r_end)]

    # DP[r][c] = (r, c)にいる状態で、お互いに最適に行動した結果、ゲーム終了時にfirstが獲得できる得点
    # DP[r_end-1][c_end-1] = 0
    # minimax
    # firstは先手、secondは後手
    # +のマスをfirstが踏んだ時、+1、-のマスをfirstが踏んだ時、-1
    # +のマスをsecondが踏んだ時、-1、-のマスをsecondが踏んだ時、+1
    # firstは得点を最大化する
    # secondは得点を最小化する
    def first_score(r, c):
        if A[r][c] == '+':
            score = 1
        else:
            score = -1
        return score

    def second_score(r, c):
        if A[r][c] == '+':
            score = -1
        else:
            score = 1
        return score

    DP = [[0]*c_end for _ in range(r_end)]
    for r in reversed(range(r_end)):
        for c in reversed(range(c_end)):
            if r == r_end-1 and c == c_end-1:
                continue
            if (r+c) % 2 == 0:
                # first
                dp = -INF
                # move_right
                if c < c_end-1:
                    score = first_score(r, c+1)
                    dp1 = DP[r][c+1] + score
                    dp = max(dp, dp1)
                # move_down
                if r < r_end - 1:
                    score = first_score(r+1, c)
                    dp2 = DP[r+1][c] + score
                    dp = max(dp, dp2)
            else:
                # second
                dp = INF
                if c < c_end-1:
                    score = second_score(r, c+1)
                    dp1 = DP[r][c+1] + score
                    dp = min(dp, dp1)
                # move_down
                if r < r_end - 1:
                    score = second_score(r+1, c)
                    dp2 = DP[r+1][c] + score
                    dp = min(dp, dp2)
            DP[r][c] = dp

    pot = DP[0][0]
    # print(pot)
    if pot >= 1:
        print('Takahashi')
    elif pot == 0:
        print('Draw')
    else:
        print('Aoki')


main()
