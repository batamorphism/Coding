def main():
    x, y = map(int, input().split('.'))
    length = len(str(y))
    y = y//(10**(length-1))
    if y >= 5:
        x += 1
    print(x)


main()
