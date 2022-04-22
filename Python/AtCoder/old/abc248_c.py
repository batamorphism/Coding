MOD = 998244353


def main():
    n, m, k = map(int, input().split())
    # DP?
    # DP[s] i番目まで見たときの、総和がsの場合における組み合わせ数
    DP = [0]*(k+1)
    DP[0] = 1
    # O(nkm)
    for _ in range(n):
        new_DP = [0]*(k+1)
        for pre_sum in range(k+1):
            for a_i in range(1, m+1):
                cur_sum = pre_sum + a_i
                if cur_sum <= k:
                    new_DP[cur_sum] += DP[pre_sum]
        for s in range(k+1):
            DP[s] = new_DP[s] % MOD

    ans = sum(DP) % MOD
    print(ans)


main()
