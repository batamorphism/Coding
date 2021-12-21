import itertools


def main():
    # input
    n, m = map(int, input().split())
    A = []
    B = []
    for _ in range(m):
        a, b = map(int, input().split())
        A.append(a-1)
        B.append(b-1)
    k = int(input())
    C = []
    D = []
    for _ in range(k):
        c, d = map(int, input().split())
        C.append(c-1)
        D.append(d-1)

    # n個の皿
    # m個の条件A[i]B[i](0=<i<=m-1)
    # kは最大で16
    ans = 0
    Bit = list(itertools.product(['C', 'D'], repeat=k))
    for bit in Bit:
        how_many_bowls = [0] * n
        for (c, d, c_or_d) in zip(C, D, bit):
            if c_or_d == 'C':
                how_many_bowls[c] += 1
            else:
                how_many_bowls[d] += 1
        pre_ans = how_many_conditions(how_many_bowls, A, B)
        if pre_ans > ans:
            ans = pre_ans

    print(ans)


def how_many_conditions(how_many_bowls, A, B):
    ret = 0
    for (a, b) in zip(A, B):
        if how_many_bowls[a] != 0 and how_many_bowls[b] != 0:
            ret += 1
    return ret


main()