# 重複組み合わせ
# w+1個から、h個を重複ありで選ぶ場合の組み合わせ
# n個からr個を重複ありで選ぶ組み合わせは、nHr = (n+r-1)Crであり
# 今回求めるのは、(w+h)C(h)である
mod = 10**9+7


def main():
    w, h = map(int, input().split())
    n = w+h-2
    r = h-1
    # calc nCr
    # = n!/r!/(n-r)!
    frac = [1]*(n+1)
    for i in range(1, n+1):
        frac[i] = (frac[i-1]*i) % mod

    ans = frac[n]*rev(frac[r])*rev(frac[n-r])
    ans %= mod
    print(ans)


def rev(x):
    # xの逆元を求める
    return pow(x, mod-2, mod)


main()
