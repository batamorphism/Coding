def main():
    n = int(input())
    solve(n)


def solve(n):
    if 2 <= n <= 4:
        print('No')
    else:
        print('Yes')
    """
    if 2**n > n ** 2:
        print('Yes')
    else:
        print('No')
    """


main()