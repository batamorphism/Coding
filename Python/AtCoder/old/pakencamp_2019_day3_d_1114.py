INF = 10**9


def main():
    N = int(input())
    S_ = [input() for _ in range(5)]
    col_dict = {'R': 0, 'B': 1, 'W': 2, '#': 3}
    S = []
    for row in S_:
        r = []
        for s in row:
            r.append(col_dict[s])
        S.append(r)

    # DP[n][col] = n列目の色がcolであるときの、塗り替えた回数
    # DP[n][col] = min(DP[n-1][not col] + cnt(n, col))
    # ただしn < 0の場合、0

    def cnt(n, col):
        # n-1列目の色をcolに染めるときの数
        ret = 0
        for r in range(5):
            if S[r][n] != col:
                ret += 1
        return ret

    DP = [[0]*5 for _ in range(N)]

    for n in range(N):
        for col in range(3):
            dp = INF
            for not_col in range(3):
                if col == not_col:
                    continue
                if n == 0:
                    dp = min(dp, cnt(n, col))
                else:
                    dp = min(dp, cnt(n, col)+DP[n-1][not_col])
            DP[n][col] = dp

    ans = INF
    for col in range(3):
        ans = min(ans, DP[N-1][col])
    print(ans)
    return


main()
