def main():
    MOD = 998244353
    n_end = int(input()) + 1
    A = [-1] + list(map(c2i, input()))
    contest_type_end = 10
    ALL = 1 << contest_type_end

    #DP[n][last][S]
    DP = [[[0]*ALL for _ in range(contest_type_end)] for _ in range(n_end)]

    # 配るDP
    for cur_n in range(n_end-1):
        # 今までn個のコンテストが開催された
        nex_n = cur_n + 1
        nex_contest_type = A[nex_n]
        for cur_S in range(ALL):
            if cur_S == 0:
                # 今までコンテストに出たことがない
                nex_S = cur_S | (1 << nex_contest_type)
                DP[nex_n][nex_contest_type][nex_S] += 1
                continue
            # 今までコンテストに出たことがある
            for last_contest_type in range(contest_type_end):
                if (cur_S & (1 << last_contest_type)) == 0:  # 矛盾
                    continue
                if DP[cur_n][last_contest_type][cur_S] == 0:
                    continue
                # nex_nに出場する場合
                # 出場が認められるのは、nex not in S or last == nex
                can_join = ((((cur_S >> nex_contest_type) & 1) == 0)
                            or (last_contest_type == nex_contest_type))
                if can_join:
                    nex_S = cur_S | (1 << nex_contest_type)
                    DP[nex_n][nex_contest_type][nex_S] += DP[cur_n][last_contest_type][cur_S]
                # nex_nに出場しない場合
                DP[nex_n][last_contest_type][cur_S] += DP[cur_n][last_contest_type][cur_S]
                DP[nex_n][last_contest_type][cur_S] %= MOD

    ans = 0
    for contest_type in range(contest_type_end):
        for S in range(ALL):
            ans += DP[n_end-1][contest_type][S]
            ans %= MOD
    print(ans)


def c2i(c):
    return ord(c) - ord('A')


main()
