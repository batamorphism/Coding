# [le, ri] := 既に食べたケーキの区間
def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]
    INF = float('inf')

    DP = [[-INF]*n for _ in range(n)]
    for cur_ate in range(n):
        for cur_le in range(n):
            cur_ri = (cur_le + cur_ate - 1) % n
            if cur_ate == 0:
                DP[cur_le][cur_ri] = 0
            # 配るDP
            is_me = cur_ate % 2 == 0
            if is_me:
                nex_le = (cur_le - 1) % n
                nex_ri = cur_ri
                DP[nex_le][nex_ri] = max(DP[nex_le][nex_ri], DP[cur_le][cur_ri] + A[nex_le])
                nex_le = cur_le
                nex_ri = (cur_ri + 1) % n
                DP[nex_le][nex_ri] = max(DP[nex_le][nex_ri], DP[cur_le][cur_ri] + A[nex_ri])
            else:
                # 大きいほうにしか遷移できない
                if A[(cur_le-1) % n] >= A[(cur_ri+1) % n]:
                    nex_le = (cur_le-1) % n
                    nex_ri = cur_ri
                else:
                    nex_le = cur_le
                    nex_ri = (cur_ri+1) % n
                DP[nex_le][nex_ri] = max(DP[nex_le][nex_ri], DP[cur_le][cur_ri])

    ans = -INF
    for le in range(n):
        ri = (le - 1) % n
        ans = max(ans, DP[le][ri])
    print(ans)


main()
