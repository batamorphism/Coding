mod = 10**9+7


def main():
    n = int(input())
    k = int(input())
    # nHk = (n+k-1)Ck
    # mCk = m!/(m-k)!k!
    m = n+k-1
    frac = [1]*(m+1)
    for i in range(1, m+1):
        frac[i] = (frac[i-1]*i) % mod

    ans = frac[m]*rev(frac[m-k])*rev(frac[k])
    ans %= mod
    print(ans)


def rev(val):
    return pow(val, mod-2, mod)


main()
