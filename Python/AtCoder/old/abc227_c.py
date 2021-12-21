def test(n):
    # n = int(input())
    val_end = n+1

    ans = 0
    for a in range(1, val_end):
        for b in range(a, val_end):
            if a*b > n:
                break
            for c in range(b, val_end):
                if a*b*c > n:
                    break
                ans += 1

    print(ans)


def main():
    n = int(input())
    a_end = int(n**(1/3))
    while a_end**3 <= n:
        a_end += 1
    # val**3 > n

    # 問題より、aは必ずn**1/3以下
    ans = 0
    for a in range(1, a_end):
        # b_end**2 * a < nでなければならない
        tmp = n//a
        b_end = int(tmp**(1/2))
        while b_end**2 <= tmp:
            b_end += 1
        for b in range(a, b_end):
            c_end = n//(a*b)
            ans += (c_end-b+1)

    print(ans)


main()
