# x**2 - y = z**2
# x**2 - z**2 = y
# (x+z)*(x-z) = y
# a = x+z, b = x-z
# b <= aとしても問題ない
# a*b = y
# x = (a+b)/2
# z = a-x
# したがって、a+bは偶数でなければならない
# 逆に、a >= b かつ a+bが偶数 かつ a+b <= 2*n かつ a*b <= nとなる(a, b)の組み合わせは、
# x**2-yが平方数となるx,yの組み合わせと1対1対応である
# したがって、bを止めてaを決める
mod = 998244353


def main():
    n = int(input())
    ans = 0
    for b in range(1, 2*n+1):
        # b <= aとなるaが対象
        # a*b <= nが条件なので、b*b > nの時点で打ち切り
        if b*b > n:
            break
        # a+bが偶数かつ、a+b <= 2*n かつ a*b <= nとなるaの数を求める
        a_max1 = 2*n-b
        if b != 0:
            a_max2 = n//b
        else:
            a_max2 = a_max1
        a_max = min(a_max1, a_max2)
        # b,..., a_maxの個数は
        if b % 2 == 0:
            # 偶数の時は、aも偶数となる
            # b, b+2, ..., a_maxの個数を求める
            a_max = a_max//2*2
            tmp = (a_max-b)//2+1
        else:
            # 奇数の時は、aもbも奇数となる
            # したがって、a_max以下の最大の奇数をとる
            if a_max % 2 == 0:
                a_max -= 1
            tmp = (a_max-b)//2+1
        ans += tmp
        ans %= mod

    print(ans)


main()
