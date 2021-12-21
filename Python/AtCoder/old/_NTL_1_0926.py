def main():
    m, n = map(int, input().split())
    p = 1000000007
    ans = pow(m, n, p)
    print(ans)


main()
