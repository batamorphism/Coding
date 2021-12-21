def main():
    n = int(input())
    k = int(input())
    p = 10**9+7
    # 1~nのn個に対して、重複してk個選ぶ場合の組み合わせの数
    # n+k-1個からk個選ぶ場合の組み合わせ数と一致
    # nCk = n!/(n-k)!/k!
    # したがって、(n+k-1)!/(n-1)!/k!を求める
    frac = [0]*(n+k)

    for i in range(n+k):
        if i <= 1:
            frac[i] = 1
        else:
            frac[i] = (i*frac[i-1]) % p

    d1 = calc_rev(frac[n-1], p)
    d2 = calc_rev(frac[k], p)
    ans = (frac[n+k-1]*d1*d2) % p
    print(ans)


def calc_rev(n, p):
    # mod p上のnの逆数を求める
    # n**(p-1) = 1 (mod p)より
    # n**(p-2) = p**-1
    return pow(n, p-2, p)


main()
