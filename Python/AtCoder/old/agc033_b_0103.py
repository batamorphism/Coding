# 独立に考える
# Taka -> Aokiの順に操作を行い
# Takaはコマを取り除きたい
# Aokiはコマを残したい
# 後ろから考える
# 終了時点で、マス目上に駒があるとAokiの勝ち。これをAoki_win_rangeとする
# Aokiは、Lがあれば、Aoki_win_rangeのRを+1できる
# Takaは、Lがあれば、Aoki_win_rangeのLを-1できる
# 途中でAoki_win_rangeが空となるか、初期状態がAoki_win_rangeに含まれていなければ、Takaの勝ち
INF = float('inf')


def main():
    r_end, c_end, turn_end = map(int, input().split())
    st_r, st_c = map(lambda x: int(x)-1, input().split())
    Taka_S = input()
    Aoki_S = input()

    def set_aoki_win_range(Aoki_win_range, Lchar, Rchar, end):
        L = 0
        R = 1
        for t in reversed(range(turn_end)):
            # Aokiの操作
            if Aoki_S[t] == Lchar:
                Aoki_win_range[R] += 1
                Aoki_win_range[R] = min(Aoki_win_range[R], end-1)
            elif Aoki_S[t] == Rchar:
                Aoki_win_range[L] -= 1
                Aoki_win_range[L] = max(Aoki_win_range[L], 0)
            # Takaの操作
            if Taka_S[t] == Lchar:
                Aoki_win_range[L] += 1
            elif Taka_S[t] == Rchar:
                Aoki_win_range[R] -= 1
            if Aoki_win_range[L] > Aoki_win_range[R]:
                Aoki_win_range[L] = INF
                Aoki_win_range[R] = -INF
                break

    # 横方向について考える
    Aoki_win_range_col = [0, c_end-1]
    Lchar = 'L'
    Rchar = 'R'
    end = c_end
    set_aoki_win_range(Aoki_win_range_col, Lchar, Rchar, end)

    # 縦方向
    Aoki_win_range_row = [0, r_end-1]
    Lchar = 'U'
    Rchar = 'D'
    end = r_end
    set_aoki_win_range(Aoki_win_range_row, Lchar, Rchar, end)

    if Aoki_win_range_row[0] <= st_r <= Aoki_win_range_row[1] and Aoki_win_range_col[0] <= st_c <= Aoki_win_range_col[1]:
        print('YES')
    else:
        print('NO')


main()
