def gcd(a, b):
    # aとbの最小公倍数を求める
    if b == 0:
        return a
    c = a % b
    return gcd(b, c)


def main():
    a, b, c = map(int, input().split())
    # a, b, cの最小公倍数を求める
    g = gcd(gcd(a, b), c)
    # 切る回数は、各辺を最小公倍数で割って、-1したものの和
    ans = 0
    for edge in [a, b, c]:
        ans += edge//g - 1

    print(ans)


main()
