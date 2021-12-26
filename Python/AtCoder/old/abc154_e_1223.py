import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)


def main():
    n = int(input())
    k = int(input())

    @lru_cache(maxsize=None)
    def F(n, k):
        if n == k == 0:
            return 1
        if n <= 0 or k < 0:
            return 0
        # 1以上n以下の整数で、
        # 0でない数がkこあるものの個数
        # 1の位で場合分け
        lo = n % 10
        nex_n = n // 10
        ret = 0
        # 1の位が0のとき
        ret += F(nex_n, k)
        # 1の位が1～loのとき
        ret += F(nex_n, k - 1)*lo
        # 1の位がlo+1～9のとき
        ret += F(nex_n-1, k - 1)*(9-lo)
        return ret

    ans = F(n, k)
    print(ans)


main()
