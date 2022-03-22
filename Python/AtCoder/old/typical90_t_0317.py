# ln2(a) < b*ln2(c)
# ln2(a) < ln2(c**b)
# a < c**b
def main():
    a, b, c = map(int, input().split())
    if a < c**b:
        print('Yes')
    else:
        print('No')


main()
