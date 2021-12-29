def main():
    a, b, c = map(int, input().split())
    # a, b, cの最小公倍数を求める
    lcm = LCM(LCM(a, b), c)
    ans = (a+b+c-3*lcm)//lcm
    print(ans)


def LCM(a: int, b: int):
    small = min(a, b)
    large = max(a, b)
    c = large % small
    while c > 0:
        large, small = small, c
        c = large % small
    return small


main()
