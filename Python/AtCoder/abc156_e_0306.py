def rev(val):
    return pow(val, MOD-2, MOD)


def nHr(n, r):
    return nCr(n+r-1, r)


def nCr(n, r):
    if n < r:
        return 0
    if r < 0:
        return 0
    return (fac[n] * fac_inv[r] * fac_inv[n-r]) % MOD


def main():
    n, k = map(int, input().split())
    # ゼロ人の部屋の数をzeroとする
    # zero人が、n-zeroの部屋に好きに移動した結果が答えとなる
    zero_min = 0
    zero_max = min(n-1, k)
    ans = 0
    for zero in range(zero_min, zero_max+1):
        #   nHr(zero, n-zero)  zero人がどの部屋に移動したか
        # * nCr(n, zero)  0人となる部屋の組み合わせ
        ans += nHr(n-zero, zero) * nCr(n, zero)
        ans %= MOD

    print(ans)


MOD = 10**9 + 7

fac_end = 10**5*4+10
fac = [1]*fac_end
fac_inv = [1]*fac_end
for i in range(1, fac_end):
    fac[i] = (fac[i-1]*i) % MOD
    fac_inv[i] = rev(fac[i])


main()
