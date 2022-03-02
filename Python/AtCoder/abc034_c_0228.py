import sys
import pypyjit
from functools import lru_cache
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**7)
MOD = 10**9+7

factorial_table = [1]*(10**6+1)
for i in range(1, 10**6+1):
    factorial_table[i] = (factorial_table[i-1] * i) % MOD

# 重複組み合わせ
# (h+1)Hwを求めればよい
def main():
    w, h = map(int, input().split())
    w -= 1
    h -= 1
    ans = nHr(h+1, w)
    print(ans)


def nHr(n, r):
    return nCr(n+r-1, r)


def nCr(n, r):
    return factorial(n) * rev(factorial(r) * factorial(n-r)) % MOD


def factorial(n):
    return factorial_table[n]


def rev(val):
    return pow(val, MOD-2, MOD)


main()
