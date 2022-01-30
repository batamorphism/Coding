def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]

    # DP[le][ri]で[le][ri]を食べた状態
    DP = [[0]*n for _ in range(n)]

    # 配るDp
    for eat in range(n):
        for cur_le in range(n):
            cur_ri = (cur_le + eat - 1) % n
            is_my_turn = eat % 2 == 0

            if is_my_turn:
                # le-1を食べる
                nex_le = (cur_le - 1) % n
                nex_ri = cur_ri
                DP[nex_le][nex_ri] = max(DP[nex_le][nex_ri], DP[cur_le][cur_ri] + A[nex_le])
                # ri+1を食べる
                nex_le = cur_le
                nex_ri = (cur_ri+1) % n
                DP[nex_le][nex_ri] = max(DP[nex_le][nex_ri], DP[cur_le][cur_ri] + A[nex_ri])
            else:
                # 大きいほうにしか遷移しない
                if A[(cur_le-1)%n] > A[(cur_ri+1)%n]:
                    # le-1を食べる
                    nex_le = (cur_le - 1) % n
                    nex_ri = cur_ri
                else:
                    nex_le = cur_le
                    nex_ri = (cur_ri+1) % n
                DP[nex_le][nex_ri] = max(DP[cur_le][cur_ri], DP[nex_le][nex_ri])

    ans = 0
    for le in range(n):
        ri = (le-1)%n
        ans = max(ans, DP[le][ri])
    print(ans)


main()
