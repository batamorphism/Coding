def main():
    n = int(input())
    ans = 0
    for a in range(1, n+1):
        if a ** 3 > n:
            break
        for b in range(a, n+1):
            if a * b**2 > n:
                break
            # cはb以上n//(a*b)以下
            c_min = b
            c_max = n // (a*b)
            ans += c_max - c_min + 1
    print(ans)


main()
