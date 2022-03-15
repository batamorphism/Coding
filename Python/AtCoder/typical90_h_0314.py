def main():
    MOD = 10**9+7
    n = int(input())
    S = input()
    T = "atcoder"
    m = len(T)

    # DP[i][j] = i文字目、j文字目まで見たときの答え
    # どっちかが0の場合は1
    DP = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        DP[i][0] = 1

    for i, s_i in enumerate(S, 1):
        for j, t_j in enumerate(T, 1):
            if s_i == t_j:
                DP[i][j] += DP[i-1][j-1]
            DP[i][j] += DP[i-1][j]
            DP[i][j] %= MOD
    ans = DP[n][m]
    print(ans)


main()
