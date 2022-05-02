def main():
    a, b, k = map(int, input().split())
    i = 0
    if a >= b:
        print(0)
        return

    while True:
        i += 1
        a *= k
        if a >= b:
            print(i)
            return


main()
