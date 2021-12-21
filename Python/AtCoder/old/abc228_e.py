mod = 998244353


def main():
    n, k, m = map(int, input().split())
    # n**k通りの数列がある
    arr_cnt = pow(k, n, mod-1)
    # arr_cnt**m通りの点数をつける方法がある
    # 求めたいのは、m**(k**n)
    if arr_cnt == 0:
        arr_cnt += (mod-1)
    ans = pow(m, arr_cnt, mod)
    print(ans)


main()
