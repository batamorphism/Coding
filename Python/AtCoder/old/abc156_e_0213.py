from functools import lru_cache
import sys
import pypyjit
pypyjit.set_param("max_unroll_recursion=-1")
sys.setrecursionlimit(10**6)

MOD = 10**9+7
frac = [1] * 10**6
for i in range(1, 10**6):
    frac[i] = frac[i-1] * i % MOD


def main():
    n, k = map(int, input().split())
    # 0人の部屋の数で全探索
    # [0, k]かつ[0, n-1]
    ans = 0
    for zero in range(min(k+1, n)):
        # n個からzero個を選び
        # n-zero個の部屋に、もともとzeroの部屋にいた人を割り当てる
        ans += nCr(n, zero) * nHr(n-zero, zero)
        ans %= MOD
    print(ans)


def nCr(n, r):
    # n!/r!/(n-r)!
    return frac[n] * rev(frac[r]) * rev(frac[n-r]) % MOD


def nHr(n, r):
    # (n+r-1)Cr
    return nCr(n+r-1, r)


def rev(val):
    return pow(val, MOD-2, MOD)


main()
