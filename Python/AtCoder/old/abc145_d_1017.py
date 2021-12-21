mod = 10**9+7


def main():
    # A*(2,1) = (3, 0) 逆もしかり となるAは
    A = [[-1, 2], [2, -1]]
    x, y = map(int, input().split())
    # A(x, y)を求める
    ax = A[0][0]*x+A[0][1]*y
    ay = A[1][0]*x+A[1][1]*y
    if ax % 3 != 0 or ay % 3 != 0 or ax < 0 or ay < 0:
        print(0)
        return
    n = ax//3+1
    k = ay//3
    # nHk = (n+k-1)!/(n-1)!/k!
    frac = [1]*(n+k)
    for i in range(1, n+k):
        frac[i] = (frac[i-1]*i) % mod
    ans = frac[n+k-1]*rev(frac[n-1])*rev(frac[k])
    ans %= mod
    print(ans)


def rev(val):
    # a**(mod-1) = 1
    return pow(val, mod-2, mod)


main()
