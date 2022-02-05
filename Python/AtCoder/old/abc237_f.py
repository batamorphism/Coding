def main():
    n, m = map(int, input().split())
    MOD = 998244353
    # DP[LISの長さ][今まで使った数の最大値][何番目まで見たか]
    DP = [[[0]*(m+1) for _ in range(4)] for _ in range(n+1)]
    for max_val in range(1, m+1):
        DP[1][1][max_val] += 1
        DP[1][0][0] += 1

    for i in range(1, n):
        for lis_len in range(4):
            if lis_len == 0:
                max_val_st = 0
                max_val_en = 1
            else:
                max_val_st = 1
                max_val_en = m+1
            for max_val in range(max_val_st, max_val_en):
                for nex_val in range(1, m+1):
                    # nex_valを使う場合
                    if nex_val > max_val:
                        # LIS更新
                        if lis_len+1 <= 3:
                            DP[i+1][lis_len+1][nex_val] += DP[i][lis_len][max_val]
                    else:
                        # LIS更新しない
                        DP[i+1][lis_len][max_val] += DP[i][lis_len][max_val]
                # nex_valを使わない場合
                DP[i+1][lis_len][max_val] += DP[i][lis_len][max_val]

    ans = 0
    for max_val in range(1, m+1):
        ans += DP[n][3][max_val]

    print(ans)


main()
