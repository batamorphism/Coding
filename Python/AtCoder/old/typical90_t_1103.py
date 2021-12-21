def main():
    a, b, c = map(int, input().split())
    # ln(a)<b*ln(c)
    # a < c**b
    if a < c**b:
        print('Yes')
    else:
        print('No')


main()
