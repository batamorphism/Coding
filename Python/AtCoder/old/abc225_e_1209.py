INF = 10**9+10


class fractions:
    def __init__(self, up, down):
        self.up = up
        self.down = down

    def __lt__(self, other):
        # self < other
        # up1/down1 < up2/down2
        # up1*down2 < down1*up2
        return self.up*other.down < self.down*other.up


def main():
    n = int(input())
    frac_pair_list = []
    fracfrac = fractions
    for i in range(n):
        x, y = map(int, input().split())
        frac1 = fracfrac(y-1, x)
        if x-1 > 0:
            frac2 = fracfrac(y, x-1)
        else:
            frac2 = fracfrac(INF, 1)
        frac_pair_list.append((frac1, frac2, i))

    # 終点でソート
    frac_pair_list.sort(key=lambda x: x[1])

    ans = 0
    last_point = fracfrac(-1, 1)
    for frac1, frac2, i in frac_pair_list:
        if not frac1 < last_point:
            last_point = frac2
            ans += 1

    print(ans)


main()
