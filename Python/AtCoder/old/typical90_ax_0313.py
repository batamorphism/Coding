def main():
    n, l = map(int, input().split())
    DP = [0]*(n+1)
    DP[0] = 1
    MOD = 10**9+7

    # 配るDP
    for cur_step in range(n+1):
        nex_step = cur_step+1
        if nex_step <= n:
            DP[nex_step] += DP[cur_step]
            DP[nex_step] %= MOD
        nex_step = cur_step + l
        if nex_step <= n:
            DP[nex_step] += DP[cur_step]
            DP[nex_step] %= MOD
    ans = DP[n]
    print(ans)


main()
