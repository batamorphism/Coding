def main():
    a, b = map(int, input().split())
    ans = gcd(a, b)
    ans = a*b//ans
    if ans > 10**18:
        ans = 'Large'
    print(ans)


def gcd(a, b):
    if a == 0:
        return b
    c = b % a
    return gcd(c, a)


main()
