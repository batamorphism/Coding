def main():
    a, b, c = map(int, input().split())
    gcd = gcd_of(gcd_of(a, b), c)
    print((a+b+c)//gcd-3)


def gcd_of(a, b):
    hi = max(a, b)
    lo = min(a, b)
    r = hi % lo
    while r > 0:
        hi = lo
        lo = r
        r = hi % lo
    return lo


main()
