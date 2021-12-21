def solver(n: int, a: int, b: int) -> int:
    """n個のボールが入っていた箱からa個取り出し、新たにb入れた

    Args:
        n (int): [description]
        a (int): [description]
        b (int): [description]

    Returns:
        int: [description]
    """
    return max(n-a, 0)+b


def main():
    # input
    n, a, b = map(int, input().split())
    ans = solver(n, a, b)
    print(ans)


main()
