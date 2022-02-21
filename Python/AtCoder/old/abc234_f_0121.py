from collections import Counter
from functools import lru_cache
MOD = 998244353


# DP[c][j] アルファベットのc番目まで使い、使った文字数の合計がjであるようなSの部分列および並び替えの個数
def main():
    S = list(map(c2i, input()))
    c_max = 26
    i_max = len(S)
    cnt_of = Counter(S)
    DP = [[0] * (i_max+1) for _ in range(c_max+1)]
    DP[0][0] = 1
    for c in range(1, c_max+1):
        for i in range(i_max+1):
            dp = 0
            k_max = min(i, cnt_of[c])
            for k in range(k_max+1):
                dp += DP[c-1][i-k]*C(i, k)
            DP[c][i] = dp % MOD
    ans = 0
    for i in range(1, i_max+1):
        ans += DP[c_max][i]
    print(ans % MOD)


def c2i(c):
    return ord(c) - ord('a') + 1


@lru_cache(maxsize=None)
def C(n, r):
    # n!/r!/(n-r)!
    return (fact(n)*rev(fact(r))*rev(fact(n-r))) % MOD


@lru_cache(maxsize=None)
def rev(x):
    return pow(x, MOD-2, MOD)


@lru_cache(maxsize=None)
def fact(n):
    if n <= 1:
        return 1
    return (n * fact(n-1)) % MOD


main()
