# 逆から考える
# 最後は、全てのマスがAokiの勝利
def main():
    r_end, c_end, n = map(int, input().split())
    st_r, st_c = map(lambda x: int(x) - 1, input().split())
    Taka_S = list(map(LRUD2tup, input()))
    Aoki_S = list(map(LRUD2tup, input()))

    # 上下、r方向に見る
    # [lo, hi] の間、Aokiが勝利
    R = 0
    C = 1
    def check(RC, st, end):
        Aoki_win_lo = 0
        Aoki_win_hi = end - 1
        for i in reversed(range(n)):
            # Aoki_Turn
            r = Aoki_S[i][RC]
            if r == -1:
                Aoki_win_hi += 1
                Aoki_win_hi = min(Aoki_win_hi, end-1)
            elif r == 1:
                Aoki_win_lo -= 1
                Aoki_win_lo = max(Aoki_win_lo, 0)
            # Taka_Turn
            r = Taka_S[i][RC]
            if r == -1:
                Aoki_win_lo += 1
            elif r == 1:
                Aoki_win_hi -= 1
            if Aoki_win_lo > Aoki_win_hi:
                return False
        if Aoki_win_lo <= st <= Aoki_win_hi:
            return True
        else:
            return False

    check_r = check(R, st_r, r_end)
    check_c = check(C, st_c, c_end)
    if check_r and check_c:
        print('YES')
    else:
        print('NO')


def LRUD2tup(c):
    if c == 'L':
        return (0, -1)
    elif c == 'R':
        return (0, 1)
    elif c == 'U':
        return (-1, 0)
    else:
        return (1, 0)


main()
