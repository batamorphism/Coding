mod = 10**9+7


def main():
    w, h = map(int, input().split())
    w -= 1
    h -= 1
    # w+hCwを求める
    frac = [1]*(w+h+1)
    for val in range(1, w+h+1):
        frac[val] = frac[val-1]*val
        frac[val] %= mod

    ans = frac[w+h]*rev(frac[w])*rev(frac[h]) % mod
    print(ans)


def rev(n):
    return pow(n, mod-2, mod)


main()
