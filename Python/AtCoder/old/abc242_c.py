MOD = 998244353


def main():
    n = int(input())
    # DP[dgt][i] dgt桁目の数字がiの時の、場合の数
    DP = [0]*10
    for i in range(n):
        new_DP = [0]*10
        if i == 0:
            # 初回処理
            for val in range(1, 10):
                new_DP[val] = 1
        else:
            for pre_val in range(1, 10):
                cur_val = pre_val
                new_DP[cur_val] += DP[pre_val]
                cur_val = pre_val - 1
                if cur_val >= 1:
                    new_DP[cur_val] += DP[pre_val]
                cur_val = pre_val + 1
                if cur_val <= 9:
                    new_DP[cur_val] += DP[pre_val]
        for val in range(10):
            DP[val] = new_DP[val] % MOD

    ans = sum(DP)
    ans %= MOD
    print(ans)


main()
