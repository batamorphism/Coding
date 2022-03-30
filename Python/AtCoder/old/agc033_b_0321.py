# 後ろから考える
def main():
    r_end, c_end, n = map(int, input().split())
    st_r, st_c = map(lambda x: int(x)-1, input().split())
    S = input()
    T = input()

    S_r = []
    S_c = []
    T_r = []
    T_c = []

    def set_SrSc(S_r, S_c, S):
        for s_i in S:
            if s_i == 'L':
                S_c.append(-1)
                S_r.append(0)
            elif s_i == 'R':
                S_c.append(1)
                S_r.append(0)
            elif s_i == 'U':
                S_c.append(0)
                S_r.append(-1)
            else:
                S_c.append(0)
                S_r.append(1)

    set_SrSc(S_r, S_c, S)
    set_SrSc(T_r, T_c, T)

    r_ans = solve(c_end, st_c, S_c, T_c, n)
    c_ans = solve(r_end, st_r, S_r, T_r, n)
    if r_ans and c_ans:
        print('YES')
    else:
        print('NO')


def solve(x_end, st_x, S_x, T_x, n):
    # 長さx_endのマス目に、今現在st_xにいる
    # SとTはそれぞれS_x, T_xにある操作を行える
    # 逆から考える
    # つまり、T->Sの順に逆の操作をしていく
    # T_win = [True]*x_end  配列だと処理が重いので、begin, endで管理
    T_win_begin = 0
    T_win_end = x_end
    for i in reversed(range(n)):
        t_i = T_x[i]
        s_i = S_x[i]
        if t_i == 1:
            # コマを右に動かすことができる
            T_win_begin -= 1
            T_win_begin = max(T_win_begin, 0)
        elif t_i == -1:
            T_win_end += 1
            T_win_end = min(T_win_end, x_end)
        # [T_win_begin, T_win_end) = nullになると負け確定
        if T_win_begin >= T_win_end:
            return False

        if s_i == 1:
            # コマを右に動かすことができる
            T_win_end -= 1
        elif s_i == -1:
            T_win_begin += 1
        # [T_win_begin, T_win_end) = nullになると負け確定
        if T_win_begin >= T_win_end:
            return False

    # [T_win_begin, T_win_end) が st_xを含んでいれば勝ち
    if T_win_begin <= st_x < T_win_end:
        return True
    else:
        return False


main()
