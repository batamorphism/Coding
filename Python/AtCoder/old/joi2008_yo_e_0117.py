# 縦のひっくり返し方を全探索
def main():
    r_end, c_end = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(r_end)]

    ans = -1
    ALL = 1 << r_end
    for bit in range(ALL):
        r_swap = [False]*r_end
        for r in range(r_end):
            if (bit >> r) & 1:
                r_swap[r] = True

        new_grid = [[0]*c_end for _ in range(r_end)]
        for r in range(r_end):
            for c in range(c_end):
                val = grid[r][c]
                if r_swap[r]:
                    if val == 0:
                        val = 1
                    else:
                        val = 0
                new_grid[r][c] = val

        ans_bit = 0
        for c in range(c_end):
            cnt_0 = 0
            cnt_1 = 0
            for r in range(r_end):
                # new_gridの1となっている数と、0となっている数
                # いずれか大きいほうをans_bitに加算
                if new_grid[r][c] == 0:
                    cnt_0 += 1
                else:
                    cnt_1 += 1
            ans_bit += max(cnt_0, cnt_1)
        ans = max(ans, ans_bit)
    print(ans)


main()
