from functools import lru_cache
from collections import Counter
import string
MOD = 998244353

factorial = [1] * 10**5
for i in range(1, 10**5):
    factorial[i] = factorial[i-1] * i % MOD


def main():
    S = list(input())
    n = len(S)
    cnt_of = Counter(S)

    total = 0
    total_of = {}
    for x in range(n+1):
        # n個からx個選ぶ組み合わせ
        total += factorial[n] * rev(factorial[n-x])
        total %= MOD

    for key, val in cnt_of.items():
        for x in range(val+1):
            # valからx個選ぶ組み合わせ
            hoge = factorial[val] * rev(factorial[val-x])
            hoge %= MOD
            total *= rev(hoge)
            print(total, hoge)
            total %= MOD

    print(total)


def char2int(char):
    # 1-indexed
    return ord(char) - ord('a') + 1


@lru_cache(maxsize=None)
def H(n, r):
    if n <= 0:
        return 1
    # nHr = (n+r-1)Cr
    nn = n+r-1
    rr = r
    # nCr = n!/(r!(n-r)!)
    ret = factorial[nn] * rev(factorial[rr]) * rev(factorial[nn-rr])
    return ret % MOD


@lru_cache(maxsize=None)
def rev(n):
    return pow(n, MOD-2, MOD)


"""
@lru_cache(maxsize=None)
def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n-1) % MOD
"""


main()
