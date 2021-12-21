def main():
    s, t, x = map(int, input().split())
    # s < tならば、 s < x < tが条件
    # s > tならば、 not (t < x < s)が条件
    x += 0.5

    if s < t:
        is_on = (s < x < t)
    else:
        is_on = not (t < x < s)
    if is_on:
        print('Yes')
    else:
        print('No')


main()
