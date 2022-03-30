def main():
    a, b, c, d = map(int, input().split())
    if a == c and b == d:
        print('Takahashi')
        return
    if a == c:
        if b <= d:
            print('Takahashi')
        else:
            print('Aoki')
        return
    if a <= c:
        print('Takahashi')
    else:
        print('Aoki')


main()
