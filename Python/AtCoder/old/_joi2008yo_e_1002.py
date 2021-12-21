def main():
    r_end, c_end = map(int, input().split())
    table = []
    for _ in range(r_end):
        row = list(map(int, input().split()))
        table.append(row)

    # r側をひっくり返すかが決まれば
    # c側をひっくり返すか否かは一意に定まる
    # rev_row_of[r] = r行目をひっくり返した
    rev_row_of = [0]*r_end
    ALL = 1 << r_end
    ans = 0
    for bit in range(ALL):
        # set rev_row_of
        for r in range(r_end):
            if bit >> r & 1:
                rev_row_of[r] = 1
            else:
                rev_row_of[r] = 0

        # calc_c
        cnt = 0
        for c in range(c_end):
            cnt_black = 0
            cnt_white = 0
            for r in range(r_end):
                is_black = table[r][c] ^ rev_row_of[r]
                if is_black:
                    cnt_black += 1
                else:
                    cnt_white += 1
                # 裏返すか否かで、blackかwhiteか大きいほうを選択できる
            cnt += max(cnt_white, cnt_black)
        ans = max(cnt, ans)

    print(ans)


main()
