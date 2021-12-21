mod = 10**9+7


def main():
    n = int(input())
    k = int(input())
    # nHkを求めよ
    # nHk = (n+k-1)Ck
    # = (n+k-1)!/(n-1)!/k!
    frac = [1]*(n+k)
    for i in range(1, n+k):
        frac[i] = (frac[i-1]*i) % mod
    ans = frac[n+k-1]*rev(frac[n-1])*rev(frac[k])
    ans %= mod
    print(ans)


def rev(val):
    # valの逆元を求める
    # a**(q-1) = 1 mod q
    # よって、a**(q-2) = a**-1
    return pow(val, mod-2, mod)


main()
