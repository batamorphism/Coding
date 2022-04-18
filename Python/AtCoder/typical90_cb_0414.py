# ほうじょ原理
def main():
    n, d = map(int, input().split())
    A = list(map(int, input().split()))

    S_end = 1 << n
    # zero_cnt[S] = Sに含まれる各a_iについて、論理積が0となるものの個数
    zero_cnt = [-1] * S_end
    for S in range(S_end):
        a_or = 0
        for i in range(n):
            if (S >> i) & 1:
                a_or |= A[i]
        # a_orとの論理積が0となる、d桁の2進数の個数
        cnt = 1 << (d-popcount(a_or))
        zero_cnt[S] = cnt

    pre_ans = 0  # いずれかのa_iとの論理積が0となる、d桁の2進数の個数
    for S in range(1, S_end):
        pc = popcount(S)
        if pc % 2 == 1:
            pre_ans += zero_cnt[S]
        else:
            pre_ans -= zero_cnt[S]

    ans = (1 << d)- pre_ans
    print(ans)


def popcount(n):
    return bin(n).count('1')


main()
