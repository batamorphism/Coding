def hoge(a, b, c):
    print(a, b, c)


def main():
    param1 = (1, 2, 3)
    param2 = (4, 5, 6)
    hoge(*param1)
    hoge(*param2)


main()
