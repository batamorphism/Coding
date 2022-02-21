def main():
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    a_next = (a + 1) % 10
    b_next = (b + 1) % 10
    if b == a_next or a == b_next:
        print('Yes')
    else:
        print('No')


main()
