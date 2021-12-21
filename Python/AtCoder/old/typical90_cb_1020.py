def count(a: int, d):
    # 0以上1<<d未満の整数xのうち、
    # a and x == 0を満たすものの数
    # これは、aを2進展開して出てくる1の数をkとして
    # 1 << (d-k)個となる
    k = bin(a)[2:].count('1')
    return 1 << (d-k)


def main():
    # 含除原理
    # (a and x != 0)を考える
    # !(a and x != 0)は、(a and x == 0)
    # いずれかのaに対し、(a and x == 0)を満たすものを考える
    # (a1 and x == 0) or (a2 and x == 0)は
    # (a1 and x == 0)+(a2 and x == 0)-((a1 or a2) and x == 0)
    n, d = map(int, input().split())
    A = list(map(int, input().split()))
    ALL = 1 << n
    ans = 0
    for bit in range(ALL):
        a = 0
        sign = -1
        for i in range(n):
            if bit >> i & 1:
                sign *= -1
                a = a | A[i]
        cnt = count(a, d)
        ans += cnt*sign
    print(-ans)


main()
