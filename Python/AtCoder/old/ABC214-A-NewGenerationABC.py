def main():
    n = int(input())
    solv(n)


def solv(n: int):
    """125までは4問
    211までは6問
    214までは8問

    Args:
        n (int): [description]
    """
    ans = 0
    if n <= 125:
        ans = 4
    elif n <= 211:
        ans = 6
    else:
        ans = 8
    print(ans)


main()