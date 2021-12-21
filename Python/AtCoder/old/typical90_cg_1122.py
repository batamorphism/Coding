def main():
    k = int(input())

    ans = 0
    for a in range(1, k + 1):
        if a*a*a > k:
            break
        if k % a != 0:
            continue
        kk = k // a
        # b*c = kkとなるb, cの組み合わせ
        for b in range(a, kk + 1):
            if b*b > kk:
                break
            if kk % b != 0:
                continue
            c = kk // b
            if c >= b:
                ans += 1

    print(ans)


main()
