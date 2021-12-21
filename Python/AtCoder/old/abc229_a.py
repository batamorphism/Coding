def main():
    S1 = input()
    S2 = input()
    if S1 == '#.' and S2 == '.#':
        print('No')
        return
    if S2 == '#.' and S1 == '.#':
        print('No')
        return
    print('Yes')


main()
