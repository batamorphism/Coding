from itertools import product


# lcs類似
def main():
    a_end, b_end = map(int, input().split())
    A = [-1] + list(map(int, input().split()))
    B = [-1] + list(map(int, input().split()))
    a_end += 1
    b_end += 1

    INF = float('inf')
    DP = [[INF]*b_end for _ in range(a_end)]
    DP[0][0] = 0
    # DP[i][j] := Aの先頭i個の要素と、Bの先頭j個の要素を使った場合の
    # 答え
    for i in range(a_end):
        DP[i][0] = i
    for j in range(b_end):
        DP[0][j] = j

    # 配るDP
    for cur_i, cur_j in product(range(a_end), range(b_end)):
        # aに1要素足す場合-ただし個の要素がbの末尾と同じケースは考える必要なし
        nex_i = cur_i + 1
        nex_j = cur_j
        if nex_i < a_end and nex_j < b_end:
            DP[nex_i][nex_j] = min(DP[nex_i][nex_j], DP[cur_i][cur_j] + 1)

        # bに1要素足す場合-同上
        nex_i = cur_i
        nex_j = cur_j + 1
        if nex_i < a_end and nex_j < b_end:
            DP[nex_i][nex_j] = min(DP[nex_i][nex_j], DP[cur_i][cur_j] + 1)

        # aとbに1要素ずつ足す場合
        nex_i = cur_i + 1
        nex_j = cur_j + 1
        if nex_i < a_end and nex_j < b_end:
            if A[nex_i] == B[nex_j]:
                DP[nex_i][nex_j] = min(DP[nex_i][nex_j], DP[cur_i][cur_j])
            else:
                DP[nex_i][nex_j] = min(DP[nex_i][nex_j], DP[cur_i][cur_j] + 1)

    ans = DP[a_end-1][b_end-1]
    print(ans)


main()
