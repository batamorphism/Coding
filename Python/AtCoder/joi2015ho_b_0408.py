def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]

    # DP[le][ri] = [le, ri)を既に取った状態における、
    # 先手が取ったピースの大きさの合計値の最大値
    n_end = n
    INF = float('inf')
    DP = [[-INF]*n_end for _ in range(n_end)]

    def move_l(piece):
        return (piece-1) % n_end

    def move_r(piece):
        return (piece+1) % n_end

    # 配るDP
    for cur_cnt in range(n_end):
        for cur_le in range(n_end):
            cur_ri = (cur_le + cur_cnt) % n_end
            # 初期化処理
            if cur_cnt == 0:
                DP[cur_le][cur_ri] = 0

            # 次に食べるのが、先手か後手か
            nex_cnt = cur_cnt + 1
            is_first = nex_cnt % 2 == 1

            # 先手の場合
            if is_first:
                # 左右のうち、より良いものを採用できる
                # 左を食べる場合
                nex_le = move_l(cur_le)
                nex_ri = cur_ri
                DP[nex_le][nex_ri] = max(DP[nex_le][nex_ri], DP[cur_le][cur_ri] + A[nex_le])
                # 右を食べる場合
                nex_le = cur_le
                nex_ri = move_r(cur_ri)
                DP[nex_le][nex_ri] = max(DP[nex_le][nex_ri], DP[cur_le][cur_ri] + A[cur_ri])
            else:
                # 左右のうち、大きい方しか採用しない
                a_le = A[move_l(cur_le)]
                a_ri = A[cur_ri]
                if a_le > a_ri:
                    # 左側を取る
                    nex_le = move_l(cur_le)
                    nex_ri = cur_ri
                    # もともと編集されているDPのほうが大きいときは、
                    # first側がうまいことやることでより最大化できる状態であるため、存置する
                    DP[nex_le][nex_ri] = max(DP[nex_le][nex_ri], DP[cur_le][cur_ri])
                else:
                    # 右側をとる
                    nex_le = cur_le
                    nex_ri = move_r(cur_ri)
                    DP[nex_le][nex_ri] = max(DP[nex_le][nex_ri], DP[cur_le][cur_ri])

    ans = -INF
    for le in range(n_end):
        for ri in range(n_end):
            ans = max(ans, DP[le][ri])

    print(ans)


main()
