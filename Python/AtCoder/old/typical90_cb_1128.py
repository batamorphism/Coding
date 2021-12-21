# a_1 & x != 0 and ... and a_n & x != 0
# 補集合は
# いずれかのa_iとのandが0
# a_1, a_2 のいずれかとのandが0 ->
# a_1とのandが0となる個数 + a_2とのandが0となる個数 - a_1とa_2とのandが0となる個数
# a_1とa_2とのandが0となる個数:=a_1 | a_2についてandが0となる個数
# a_1 and ... and a_n and x == 0


def main():
    n, d = map(int, input().split())
    A = list(map(int, input().split()))

    def cnt_x_of(a):
        # aとのandが0となるd桁のxの個数
        # これは、aを2進数展開した時の1が出てくる個数をxとして
        # 2**(d-x)が答え
        x = 0
        while a > 0:
            if a & 1 == 1:
                x += 1
            a >>= 1
        return 2**(d-x)

    ans = 0
    ALL_a = 1 << n
    for bit_a in range(ALL_a):
        cnt = 0
        sub_A = []
        for i in range(n):
            if (bit_a >> i) & 1:
                cnt += 1
                sub_A.append(A[i])
        a_or = 0
        for a in sub_A:
            a_or |= a
        cnt_x = cnt_x_of(a_or)
        if cnt % 2 == 0:
            ans += cnt_x
        else:
            ans -= cnt_x

    print(ans)


main()
