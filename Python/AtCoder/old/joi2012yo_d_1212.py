import sys
sys.setrecursionlimit(10**6)

# DP(n, cur, bef1, bef2) = 前日にbef1を、前々日にbef2を選んだ時に、n日目にcurを選ぶ組み合わせ数

mod = 10_000


def main():
    n, k = map(int, input().split())
    rules = [0]*(n+1)
    for _ in range(k):
        a, b = map(int, input().split())
        rules[a] = b

    # rules[day]のパスタはbのみ

    def dp(day, cur, bef1, bef2):
        if (day, cur, bef1, bef2) in dp.cache:
            return dp.cache[day, cur, bef1, bef2]
        ret = 0
        if rules[day] != 0:
            if cur != rules[day]:
                # dayに食べるパスタが定められている場合、該当しないケースを0にする
                dp.cache[day, cur, bef1, bef2] = 0
                return 0
        if day == 0:
            ret = 1
        elif day == 1:
            # 0は、パスタを食べていないことを表す
            ret = dp(day-1, 0, 0, 0)
        elif day == 2:
            ret = dp(day-1, bef1, 0, 0)
        elif day == 3:
            ret = dp(day-1, bef1, bef2, 0)
        else:
            # dp(day-1, bef1, bef2, any)の総和
            for bef3 in range(1, 4):
                if bef1 == bef2 == bef3:
                    continue
                ret += dp(day-1, bef1, bef2, bef3)
        ret %= mod
        dp.cache[day, cur, bef1, bef2] = ret
        return ret
    dp.cache = {}

    ans = 0
    for cur in range(1, 4):
        for bef1 in range(1, 4):
            for bef2 in range(1, 4):
                if cur == bef1 == bef2:
                    continue
                ans += dp(n, cur, bef1, bef2)
    ans %= mod
    print(ans)
    # print(dp.cache)
    # dp_ = sorted(dp.cache.items())
    # for key, val in dp_:
    #     print(key, val)


main()
