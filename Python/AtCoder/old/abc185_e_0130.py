# DP[i][j] a_i, b_iまで見た時の答え
from operator import ne


def main():
    INF = float('inf')
    a_end, b_end = map(int, input().split())
    a_end += 1
    b_end += 1
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))

    DP = [[INF] * b_end for _ in range(a_end)]
    # 初期値の設定
    for i in range(a_end):
        for j in range(b_end):
            DP[i][j] = max(i, j)
    # 配るDP
    for cur_i in range(a_end):
        for cur_j in range(b_end):
            # 右に遷移
            nex_i = cur_i + 1
            nex_j = cur_j
            if nex_i < a_end:
                DP[nex_i][nex_j] = min(DP[nex_i][nex_j], DP[cur_i][cur_j] + 1)
                # 一致している場合は、斜めの遷移でカバーされる
            # 下に遷移
            nex_i = cur_i
            nex_j = cur_j + 1
            if nex_j < b_end:
                DP[nex_i][nex_j] = min(DP[nex_i][nex_j], DP[cur_i][cur_j] + 1)
            # 斜めに遷移
            nex_i = cur_i + 1
            nex_j = cur_j + 1
            if nex_i < a_end and nex_j < b_end:
                if A[nex_i] == B[nex_j]:
                    DP[nex_i][nex_j] = min(DP[nex_i][nex_j], DP[cur_i][cur_j])
                else:
                    DP[nex_i][nex_j] = min(DP[nex_i][nex_j], DP[cur_i][cur_j] + 1)
    ans = DP[-1][-1]
    print(ans)


main()
