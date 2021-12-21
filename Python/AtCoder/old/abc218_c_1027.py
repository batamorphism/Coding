def rotate(S):
    S = S[::-1]  # 反転
    S = tuple(zip(*S))  # 転置
    return S


def get_left_high(S):
    #  左上の#を見つける
    r_end = c_end = len(S)
    for r in range(r_end):
        for c in range(c_end):
            if S[r][c] == '#':
                return r, c


def match(S, T):
    sr0, sc0 = get_left_high(S)
    tr0, tc0 = get_left_high(T)
    offset_r = tr0-sr0
    offset_c = tc0-sc0
    r_end = c_end = len(S)
    for r in range(r_end):
        for c in range(c_end):
            if S[r][c] == '#':
                if not (0 <= r+offset_r < r_end and 0 <= c+offset_c < c_end):
                    return False
                if T[r+offset_r][c+offset_c] != '#':
                    return False
    return True


def solver(S: tuple, T: tuple):
    # まずは数が一致しているか
    cnt_s, cnt_t = 0, 0
    for s in S:
        cnt_s += s.count('#')
    for t in T:
        cnt_t += t.count('#')
    if cnt_s != cnt_t:
        return False
    # 形が一致するか
    for _ in range(4):
        exist = match(S, T)
        if exist:
            return True
        S = rotate(S)
    return False


def main():
    n = int(input())
    S = tuple([tuple(input()) for _ in range(n)])
    T = tuple([tuple(input()) for _ in range(n)])
    # S = S[::-1]  # 反転
    # S = tuple(zip(*S))  # 転置
    if solver(S, T):
        print('Yes')
    else:
        print('No')


main()
