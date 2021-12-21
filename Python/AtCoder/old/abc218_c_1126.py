def main():
    n = int(input())
    S = []
    for _ in range(n):
        s_r = tuple(input())
        S.append(s_r)

    T = []
    for _ in range(n):
        t_r = tuple(input())
        T.append(t_r)

    is_same = False
    if check_cnt(S, T):
        if check_rotate(S, T):
            is_same = True
        else:
            is_same = False
    else:
        is_same = False

    if is_same:
        print('Yes')
    else:
        print('No')


def check_cnt(S, T):
    # SとTに含まれる#の数が同じか
    r_end = c_end = len(S)
    S_cnt = 0
    T_cnt = 0
    for r in range(r_end):
        for c in range(c_end):
            if S[r][c] == '#':
                S_cnt += 1
            if T[r][c] == '#':
                T_cnt += 1
    return S_cnt == T_cnt


def check_rotate(S, T):
    is_same = False
    for _ in range(4):
        S = rotate(S)
        if shift_same(S, T):
            is_same = True
            break
    return is_same


def shift_same(S, T):
    # SとTは、平行移動したら同じになるかを確認する
    r_end = c_end = len(S)
    S_lo_r, S_lo_c = get_lo_rc(S)
    T_lo_r, T_lo_c = get_lo_rc(T)
    offset_r, offset_c = T_lo_r - S_lo_r, T_lo_c - S_lo_c
    for s_r in range(r_end):
        for s_c in range(c_end):
            if S[s_r][s_c] == '#':
                t_r, t_c = s_r + offset_r, s_c + offset_c
                if not (0 <= t_r < r_end and 0 <= t_c < c_end):
                    return False
                if not T[t_r][t_c] == '#':
                    return False
    return True


def get_lo_rc(S):
    # 最も上の最も左にある#の位置を返す
    r_end = c_end = len(S)
    for r in range(r_end):
        for c in range(c_end):
            if S[r][c] == '#':
                return (r, c)
    # Sは必ず#を含む


def rotate(S):
    # Sを90度回転させる
    S = tuple(zip(*S[::-1]))
    return S


main()
