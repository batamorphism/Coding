def main():
    MOD = 998244353

    n = int(input())
    dgt = 1
    # 各桁についてみていく
    ans = 0
    for dgt in range(1, 20):
        if 10 ** (dgt-1) > n:
            break
        # dgt桁について
        # f(10**(dgt-1)) + ,... + f(10**dgt-1)を計算する
        # 1 + ... + (10**dgt-1) - 10**(dgt - 1) + 1
        st_val = 1
        en_val = min(n, (10**dgt - 1)) - 10 ** (dgt - 1) + 1
        cnt = (st_val + en_val) * (en_val - st_val + 1) // 2
        ans += cnt
        ans %= MOD

    print(ans)


main()
