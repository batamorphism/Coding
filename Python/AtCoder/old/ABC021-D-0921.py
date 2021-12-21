p = 10**9+7


def main():
    n = int(input())
    k = int(input())

    # fac[n] = n!
    fac = [0]*(n+k)
    for i in range(n+k):
        if i <= 1:
            fac[i] = 1
        else:
            fac[i] = (i*fac[i-1]) % p

    # r_fac[n] = n!のmod pの逆元
    # x^-1 = x^(p-2) % p フェルマーの小定理a**p-1 = 1より
    r_fac = [0]*(n+k)
    for i in range(n+k):
        # calc x**(p-2) % p
        x = fac[i]
        tmp = 1
        pp_bin = bin(p-2)[2:]  # 先頭の0bを取り除く
        for bit in pp_bin:
            tmp = tmp ** 2 % p
            if bit == 'b':
                tmp = 1
                continue
            if bit == '1':
                tmp = tmp * x % p

        r_fac[i] = tmp

    print(comb(n+k-1, k, fac, r_fac))


def comb(n, k, fac, r_fac):
    # pは素数
    # fac(n)//fac(n-k)//fac(k)を求める
    # ただし、mod p 上で割り算はそのままではうまくいかないので
    # 逆元を求めておく
    return (fac[n]*r_fac[n-k]*r_fac[k]) % p


main()
