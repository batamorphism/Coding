def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]

    # DP[i][j] = [i, j]のケーキが残っている状態で、そこから追加で取れる分
    # DP[i][i] = iだけが残っている状態
    # DP[i][i-1] = 全部残っている状態
    DP = [[0]*n for _ in range(n)]
    for di in range(n):
        for le in range(n):
            ri = le+di
            ri %= n
            ate = n-di-1
            # 既に食べたケーキ数が偶数の場合は、meのターン
            # 奇数の場合は、heのターン
            is_me = ate % 2 == 0
            if is_me:
                # di == 0の時は、最初に呼ばれるのでDP[*][*]==0だからよし!
                get_le = DP[(le+1) % n][ri]+A[le]
                get_ri = DP[le][(ri-1) % n]+A[ri]
                DP[le][ri] = max(get_le, get_ri)
            else:
                if A[le] > A[ri]:
                    dp = DP[(le+1) % n][ri]
                else:
                    dp = DP[le][(ri-1) % n]
                DP[le][ri] = dp

    ans = 0
    for le in range(n):
        ri = (le-1) % n
        ans = max(DP[le][ri], ans)
    print(ans)


main()
