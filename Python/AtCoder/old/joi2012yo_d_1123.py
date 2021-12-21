mod = 10_000


def main():
    n, k = map(int, input().split())
    day_end = n
    B = [-1]*day_end
    for _ in range(k):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        B[a] = b

    memo = {}
    def dp(day, col, bef):
        if (day, col, bef) in memo:
            return memo[(day, col, bef)]
        ret = 0
        if B[day] != -1 and B[day] != col:
            ret = 0
        elif day == 0:
            if bef == (col+1) % 3:
                ret = 1
            else:
                ret = 0
        else:
            for bef1 in range(3):
                # col-bef-bef1の組み合わせ
                if col == bef and bef1 == bef:
                    continue
                ret += dp(day-1, bef, bef1)
        ret %= mod
        memo[(day, col, bef)] = ret
        return ret

    ans = 0
    for col in range(3):
        for bef in range(3):
            ans += dp(day_end-1, col, bef)
    ans %= mod

    print(ans)


main()
