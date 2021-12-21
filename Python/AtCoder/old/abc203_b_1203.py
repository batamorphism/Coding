def main():
    S = input()
    # oxxoxxoxx...
    # xxoxxoxxo...
    # xoxxoxxox...
    check1 = True
    for i, s in enumerate(S):
        if i % 3 == 0:
            c = 'o'
        else:
            c = 'x'
        if s != c:
            check1 = False
            break
    check2 = True
    for i, s in enumerate(S):
        if i % 3 == 1:
            c = 'o'
        else:
            c = 'x'
        if s != c:
            check2 = False
            break
    check3 = True
    for i, s in enumerate(S):
        if i % 3 == 2:
            c = 'o'
        else:
            c = 'x'
        if s != c:
            check3 = False
            break

    check = check1 or check2 or check3
    if check:
        print('Yes')
    else:
        print('No')


main()
