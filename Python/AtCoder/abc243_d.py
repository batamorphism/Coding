def main():
    n, x = map(int, input().split())
    S = list(input())
    # Uを潰す
    # Uは、直前のLかRを無視する
    que = []
    for c in S:
        if c == 'U' and que and que[-1] != 'U':
            que.pop()
        else:
            que.append(c)
    # queに従い、nを移動させる
    for c in que:
        if c == 'U':
            x //= 2
        elif c == 'L':
            x *= 2
        else:
            x *= 2
            x += 1

    print(x)


main()
