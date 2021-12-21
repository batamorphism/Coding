from functools import lru_cache


def main():
    n = int(input())
    k = int(input())

    @lru_cache(maxsize=None)
    def F(n, k):
        if n == k == 0:
            return 1
        if n <= 0 or k < 0:
            return 0
        # 0以上n以下の整数で、0出ない数字がちょうどk個あるものの個数
        # 1の位で場合分けする
        num_1 = n % 10
        nex_n = n // 10
        ret = 0
        # 1, .., num_1までの和
        ret += F(nex_n, k-1) * num_1
        # num_1+1, ...9までの和
        ret += F(nex_n-1, k-1) * (9 - num_1)
        ret += F(nex_n, k)
        return ret

    ans = F(n, k)
    print(ans)


main()
