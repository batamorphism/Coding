def main():
    n = int(input())

    ans = 0
    for a in range(1, n + 1):
        if a**3 > n:
            break
        for b in range(a, n + 1):
            if a*b*b > n:
                break
            # a*b*c <= nとなる最大のcを求める
            # c <= n/a/b
            c = n // (a*b)
            while a*b*(c+1) <= n:
                c += 1
            while a*b*c > n:
                c -= 1
            # b <= k <= c
            # print(a, b, c)
            ans += c - b + 1

    print(ans)


main()
