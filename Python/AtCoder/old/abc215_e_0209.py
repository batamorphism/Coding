# bitDPは配るDP
def main():
    n = int(input())
    n += 1
    S = [-1] + list(map(c2i, input()))
    type_end = 10
    ALL = 1 << type_end
    MOD = 998244353

    DP = [[0]*ALL for _ in range(type_end)]
    for cur_i in range(n-1):
        nex_DP = [[0]*ALL for _ in range(type_end)]
        nex_i = cur_i+1
        nex_type = S[nex_i]
        # nex_typeに初めて出場する場合
        nex_DP[nex_type][1 << nex_type] += 1
        # 既に一度以上出場したことがある場合
        for cur_last in range(type_end):
            for cur_S in range(1, ALL):
                if cur_last == nex_type:
                    # 現在、cur_Sに出場済みで、cur_lastが最後に出場したもの
                    nex_S = cur_S
                    nex_DP[cur_last][nex_S] += DP[cur_last][cur_S]  # nex_iに出場しない
                    nex_DP[nex_type][nex_S] += DP[cur_last][cur_S]  # nex_iに出場する
                else:
                    # nex_typeに
                    # まだnex_typeに出場したことがない場合のみ、出場可能
                    if cur_S >> nex_type & 1 == 0:
                        nex_S = cur_S | 1 << nex_type
                        nex_DP[nex_type][nex_S] += DP[cur_last][cur_S]  # nex_iに出場する
                    nex_DP[cur_last][cur_S] += DP[cur_last][cur_S]  # nex_iに出場しない
        for cur_last in range(type_end):
            for cur_S in range(ALL):
                DP[cur_last][cur_S] = nex_DP[cur_last][cur_S] % MOD

    ans = 0
    for cur_last in range(type_end):
        ans += sum(DP[cur_last]) % MOD
    ans %= MOD
    print(ans)


def c2i(c):
    return ord(c) - ord('A')


main()
