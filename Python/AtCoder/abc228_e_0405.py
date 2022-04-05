MOD = 998244353


def main():
    n, k, m = map(int, input().split())

    # 数列は、k種類の数字をn個選ぶので、
    # k**nとおり
    # k**nとおりに対し、mとおりの整数を割り当てるので
    # m**(k**n)が答え

    # a**(mod-1) = 1 であるから
    # t = pow(k, n)としたときに、
    # tがmod-1の倍数であるときは0(mod上)としたい
    t = pow(k, n, MOD-1)
    if t == 0:
        t = MOD-1
    ans = pow(m, t, MOD)
    print(ans)


main()
