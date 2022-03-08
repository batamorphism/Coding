def main():
    a, b, c, x = map(int, input().split())
    if x <= a:
        print(1)
        return
    elif x > b:
        print(0)
        return
    else:
        cnt = b-a
        print(c/cnt)


main()
