def main():
    MOD = 10**9+7
    k = int(input())

    if k % 9 != 0:
        print(0)
        return

    # k % 9 == 0であれば、答えがある
    # 各桁の総和がxとなるものがいくつあるかをdp[x]と置く
    # 配るdp
    dp = [0]*(k+1)
    dp[0] = 1
    for cur_i in range(k+1):
        dp_cur_i = dp[cur_i]
        for val in range(1, 10):
            nex_i = cur_i + val
            if nex_i > k:
                break
            dp[nex_i] += dp_cur_i
            dp[nex_i] %= MOD

    ans = dp[k] % MOD
    print(ans)


main()
