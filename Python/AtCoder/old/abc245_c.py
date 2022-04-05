def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    """
    n = 2*10**5
    k = 10**5
    A = [i for i in range(10**8, 10**8+n)]
    B = [i for i in range(10**8, 10**8+n)]
    """

    DP = set([A[0], B[0]])  # x_iとして取りうる数
    for a_i, b_i in zip(A[1:], B[1:]):
        new_DP = set()
        for pre_x in DP:
            if k >= abs(pre_x - a_i):
                new_DP.add(a_i)
            if k >= abs(pre_x - b_i):
                new_DP.add(b_i)
        DP = set()
        for x in new_DP:
            DP.add(x)

    if DP:
        print('Yes')
    else:
        print('No')


main()
