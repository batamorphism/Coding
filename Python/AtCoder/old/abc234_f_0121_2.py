from collections import Counter
MOD = 998244353


# DP[c][j] アルファベットのc番目まで使い、使った文字数の合計がjであるような
# Sの部分列および並び替えの個数
def main():
    S = list(map(c2i, input()))
    c_max = 26
    i_max = len(S)

    fact = [1] * (i_max + 10)
    for i in range(1, i_max + 10):
        fact[i] = (fact[i-1] * i) % MOD

    rev_fact = [1] * (i_max + 10)
    for i, f in enumerate(fact):
        rev_fact[i] = pow(f, MOD - 2, MOD)

    def comb(n, r):
        return fact[n]*rev_fact[r] % MOD*rev_fact[n-r] % MOD

    cnt_of = Counter(S)
    DP = [[0] * (i_max+1) for _ in range(c_max+1)]
    DP[0][0] = 1
    for c in range(1, c_max+1):
        for i in range(i_max+1):
            dp = 0
            k_max = min(i, cnt_of[c])
            for k in range(k_max+1):
                dp += DP[c-1][i-k]*comb(i, k)
                dp %= MOD
            DP[c][i] = dp % MOD
    ans = 0
    for i in range(1, i_max+1):
        ans += DP[c_max][i]
        ans %= MOD
    print(ans % MOD)


def c2i(c):
    return ord(c) - ord('a') + 1


main()
