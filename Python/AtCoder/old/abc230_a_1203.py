def main():
    n = int(input())
    if n >= 42:
        n += 1
    ans = format(n, '03')
    ans = 'AGC' + ans
    print(ans)


main()
