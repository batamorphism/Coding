from collections import Counter
MOD = 998244353

factorial_table = [1] * 5001
for i in range(1, 5001):
    factorial_table[i] = factorial_table[i-1]*i % MOD

comb_table = [[0] * 5001 for _ in range(5001)]
for n in range(5001):
    for r in range(n+1):
        if n == r or r == 0:
            comb_table[n][r] = 1
            continue
        comb_table[n][r] = (comb_table[n-1][r-1] + comb_table[n-1][r]) % MOD


def main():
    S = input()
    n = len(S)
    cnt_of = Counter(S)

    dp = [0]*(n+1)
    for char, num in cnt_of.items():
        new_dp = [0]*(n+1)
        # 今回初めて使う場合
        cur_num = 0
        for nex_num in range(1, num+1):
            new_dp[nex_num] += 1
        # 前回、i文字使ってる場合
        # 今回新たにadd_num個使うと、i+add_num文字使う
        for cur_num in range(1, n+1):
            for nex_add in range(num+1):
                nex_num = cur_num+nex_add
                if nex_num > n:
                    break
                # nex_num文字からnex_add文字を選ぶ組み合わせ数
                new_dp[nex_num] += dp[cur_num] * comb_table[nex_num][nex_add]
        for i in range(n+1):
            dp[i] = new_dp[i]
            dp[i] %= MOD

    ans = sum(dp) % MOD
    print(ans)


def comb(n, r):
    # n!/r!/(n-r)! をmodで割ったあまりを返す
    return comb_table[n][r]


main()
