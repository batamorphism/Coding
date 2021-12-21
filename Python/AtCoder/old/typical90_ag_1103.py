def main():
    h, w = map(int, input().split())
    if h == 1:
        print(w)
        return
    elif w == 1:
        print(h)
        return

    if h % 2 != 0:
        h += 1
    if w % 2 != 0:
        w += 1
    print(h*w//4)


main()
