mod = 10**9+7


def main():
    x, y = map(int, input().split())
    # 1, 2 -> 0, 1
    # 2, 1 -> 1, 0
    # 2 -1
    # -1 2
    # を乗じたあと3で割る
    x, y = 2*x-y, -x+2*y
    if x % 3 != 0 or y % 3 != 0:
        print(0)
        return
    x, y = x//3, y//3
    if x < 0 or y < 0:
        print(0)
        return

    def rev(a):
        # a**(p-1) = 1
        return pow(a, mod-2, mod)

    # (x+y)からx個を選ぶ組み合わせ数
    frac = [1]*(x+y+1)
    for i in range(1, x+y+1):
        frac[i] = frac[i-1]*i
        frac[i] %= mod

    ans = (frac[x+y]*rev(frac[x])*rev(frac[y])) % mod
    print(ans)


main()
