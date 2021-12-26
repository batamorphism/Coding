mod = 998244353


def main():
    # 各数列に対し、m通りの点数が付く
    # 各数列は、k**n通り存在する
    # m**(k**n)を求める
    n, k, m = map(int, input().split())
    # print((m**(k**n)) % mod)

    if m % mod == 0:
        print(0)
        return

    # a**(mod-1) = 1 (mod) <- aとpは互いに素の時
    # したがって、m**x = m**(x-(mod-1))
    x = pow(k, n, mod-1)
    x += (mod-1)
    ans = pow(m, x, mod)
    print(ans)


main()
