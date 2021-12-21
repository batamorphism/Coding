def main():
    # A[0] and X == 0を満たす数をf(0)と置く
    # A[0] and X != 0を満たす数はALL-f(0)
    # (A[0] and X == 0) and (A[1] and X == 0)を満たす数をf(0, 1)と置く
    # これは、(A[0] or A[1]) and X == 0 を満たす数に等しい
    n, d = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    ALL = 1 << n
    for bit in range(ALL):
        a = 0
        cnt = 0
        for i in range(n):
            if bit >> i & 1:
                cnt += 1
                a = a | A[i]
        if cnt % 2 == 0:
            ans += f(a, d)
        else:
            ans -= f(a, d)
    print(ans)


def f(bit: int, d: int):
    cnt = bin(bit)[2:].count('1')
    return 2**(d-cnt)


main()
