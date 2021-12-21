# (r, c)を左上として、畳を敷く
# r*c <= 16より、全列挙が可能
# tupleのtupleで状態を管理する
ans = 0


def main():
    r_end, c_end, gr_max, lo_max = map(int, input().split())
    # grが1*2の畳、loが1*1の畳
    grid = tuple([tuple([0]*c_end) for _ in range(r_end)])
    # バックトラックで畳を敷く

    def nex_of(pre_r, pre_c):
        cur_r = pre_r
        cur_c = pre_c + 1
        if cur_c == c_end:
            cur_r += 1
            cur_c = 0
        return cur_r, cur_c

    def dfs(pre_r, pre_c, pre_gr, pre_lo, grid):
        if pre_r == r_end:
            global ans
            ans += 1
            # print("---" + str(ans))
            # for g in grid:
            #     print(g)
            return
        cur_r, cur_c = nex_of(pre_r, pre_c)
        if grid[pre_r][pre_c]:
            # 既に畳が敷いてあるときは次に
            dfs(cur_r, cur_c, pre_gr, pre_lo, grid)
        else:
            # 畳を敷く
            if pre_lo < lo_max:
                grid_1 = tuple_to_list(grid)
                grid_1[pre_r][pre_c] = 1
                grid_1 = list_to_tuple(grid_1)
                dfs(cur_r, cur_c, pre_gr, pre_lo+1, grid_1)
            if pre_gr < gr_max:
                if pre_r + 1 < r_end and grid[pre_r+1][pre_c] == 0:
                    grid_2 = tuple_to_list(grid)
                    grid_2[pre_r][pre_c] = 2
                    grid_2[pre_r+1][pre_c] = 2
                    grid_2 = list_to_tuple(grid_2)
                    dfs(cur_r, cur_c, pre_gr+1, pre_lo, grid_2)
                if pre_c + 1 < c_end and  grid[pre_r][pre_c+1] == 0:
                    grid_3 = tuple_to_list(grid)
                    grid_3[pre_r][pre_c] = 3
                    grid_3[pre_r][pre_c+1] = 3
                    grid_3 = list_to_tuple(grid_3)
                    dfs(cur_r, cur_c, pre_gr+1, pre_lo, grid_3)

    dfs(0, 0, 0, 0, grid)
    print(ans)


def tuple_to_list(tup):
    # tupleのtupleをlistのlistに変換
    ret = []
    for t in tup:
        ret.append(list(t))
    return ret


def list_to_tuple(lst):
    # listのlistをtupleのtupleに変換
    ret = []
    for ls in lst:
        ret.append(tuple(ls))
    return tuple(ret)


main()

