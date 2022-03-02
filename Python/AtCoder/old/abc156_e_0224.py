MOD = 10**9 + 7

fac = [1]*(10**5*5+1)
rev_fac = [1]*(10**5*5+1)
for i in range(1, 10**5*5+1):
    fac[i] = (fac[i-1]*i) % MOD
    rev_fac[i] = pow(fac[i], MOD-2, MOD)


def nCr(n, r):
    return (fac[n]*rev_fac[r]*rev_fac[n-r]) % MOD


def nHr(n, r):
    return nCr(n+r-1, r)


def main():
    n, k = map(int, input().split())
    # zero人が、n-zero個の部屋に重複ありで移動する nHr(n-zero, k)
    # n個の部屋から0任の部屋をzero個探す nCr(n, zero)
    ans = 0
    for zero in range(min(n, k+1)):
        # print(zero, nCr(n, zero), nHr(n-zero, zero))
        ans += nCr(n, zero) * nHr(n-zero, zero)
        ans %= MOD
    print(ans)


main()
