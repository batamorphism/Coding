def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [None]*(m+1)

    # あるcに対し
    # a_dim + b_dim = c_dim
    # を満たすすべてのa, bについて総和を取る
    for c_dim in range(n+m+1):
        ab_sum = 0
        for a_dim in reversed(range(min(c_dim+1, n+1))):
            b_dim = c_dim - a_dim
            if not (0 <= b_dim <= m):
                continue
            if not (0 <= a_dim <= n):
                continue
            if B[b_dim] is None:
                if A[a_dim] != 0:
                    B[b_dim] = (C[c_dim]-ab_sum)//A[a_dim]
                else:
                    # A[a_dim]*B[b_dim] + ab_sum = C[c_dim]
                    pass
            else:
                ab_sum += A[a_dim]*B[b_dim]
    print(*B)


main()
