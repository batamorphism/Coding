# 素因数分解
# 42 = 2*3*7 = 3個
# 一回の操作で素因数を半分にすることができる
# 3->1+2->1

# したがって答えは、素因数の個数の切り上げ
def main():
    n = int(input())
    factor_list = []
    for fac in range(2, n):
        if fac**2 > n:
            break
        while n % fac == 0:
            n //= fac
            factor_list.append(fac)
    if n != 1:
        factor_list.append(n)

    # print(factor_list)
    cnt = len(factor_list)
    ans = 0
    while cnt != 1:
        ans += 1
        cnt = -(-cnt // 2)

    print(ans)


main()
