import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)


# 桁DP
def main():
    n = int(input())
    k = int(input())

    @lru_cache(maxsize=None)
    def f(n, k):
        # n, kに対する答え
        # n= 432の時
        # 1桁目が0であれば、f(n//10, k)
        # 1桁目が1, 2であれば、f(n//10, k-1)
        # 3以上であれば、f(n//10-1, k-1)]
        if n == 0 and k == 0:
            return 1
        elif n <= 0 or k < 0:
            return 0
        ret = 0
        num = n % 10
        ret += f(n//10, k)
        ret += f(n//10, k-1)*num
        ret += f(n//10-1, k-1)*(9-num)
        return ret

    ans = f(n, k)
    print(ans)


main()
