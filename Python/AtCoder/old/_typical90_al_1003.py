def main():
    a, b = map(int, input().split())
    g = gcm(a, b)
    if a*b//g > 10**18:
        print('Large')
        return
    print(a*b//g)


def gcm(a, b):
    hi = max(a, b)
    lo = min(a, b)
    c = hi % lo
    while c > 0:
        hi = lo
        lo = c
        c = hi % lo
    return lo


main()
