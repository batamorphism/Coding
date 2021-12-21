import sys
sys.setrecursionlimit(10**9)
mod = 10**5


def main():
    n, k = map(int, input().split())

    def one_step(x):
        y = 0
        for num_str in str(x):
            num = int(num_str)
            y += num
        return (x+y) % mod

    memo = {}  # (n, cnt) -> val 最初がnの操作をcnt回行った後の結果
    def many_step(x, cnt):
        if (x, cnt) in memo:
            return memo[(x, cnt)]
        if cnt == 0:
            return x
        if cnt == 1:
            return one_step(x)
        le = cnt >> 1
        ri = cnt - le
        y = many_step(x, le)
        ret = many_step(y, ri)
        memo[(x, cnt)] = ret
        return ret

    ans = many_step(n, k)

    print(ans)


main()
