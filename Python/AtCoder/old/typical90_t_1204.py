# log2(a) < b*log2(c)
# a < c**b
def main():
    a, b, c = map(int, input().split())
    le = a
    ri = c**b
    if le < ri:
        print('Yes')
    else:
        print('No')


main()
