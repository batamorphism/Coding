def main():
    h, w = map(int, input().split())
    if h == 1:
        print(w)
        return
    if w == 1:
        print(h)
        return
    # 2で割って切りあげする
    h = -(-h//2)
    w = -(-w//2)
    ans = h*w
    print(ans)


main()
