def main():
    a, b = map(int, input().split())
    c = gcd(a, b)
    # 答えは、a*b/c
    #       a*b/c > 10**18
    # <->   1/c > 10**18/a/b
    if 1 > (10**18/a/b)*c+0.000001:
        print('Large')
    else:
        ans = a*b//c
        if ans > 10**18:
            print('Large')
        else:
            print(a*b//c)


def gcd(a, b):
    hi = max(a, b)
    lo = min(a, b)
    q = hi % lo
    while q > 0:
        hi = lo
        lo = q
        q = hi % lo
    return lo


main()
