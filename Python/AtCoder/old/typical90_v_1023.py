def gcd(a, b):
    lo = min(a, b)
    hi = max(a, b)
    q = hi % lo
    while q > 0:
        hi, lo = lo, q
        q = hi % lo
    return lo


def main():
    a, b, c = map(int, input().split())
    gcd_of_abc = gcd(gcd(a, b), c)
    ans = 0
    ans += a//gcd_of_abc-1
    ans += b//gcd_of_abc-1
    ans += c//gcd_of_abc-1
    print(ans)


main()
