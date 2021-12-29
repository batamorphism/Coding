def main():
    x, y = map(int, input().split())
    for cnt in range(1000):
        val = x + cnt*10
        if val >= y:
            ans = cnt
            break
    print(ans)


main()
