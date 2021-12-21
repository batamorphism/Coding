# 3**16 = 43_046_721 = 10^7
ans = 0

def main():
    global ans
    r_end, c_end, large_max, small_max = map(int, input().split())

    # 0だと畳が敷いてある、1だと小さい畳
    # 2だと横に大きい畳
    # 3だと縦に大きい畳
    grid = [[0]*c_end for _ in range(r_end)]

    def rc2ind(r, c):
        return r*c_end + c

    def ind2rc(ind):
        r = ind // c_end
        c = ind % c_end
        return r, c

    ind_end = r_end*c_end

    def dfs(pre_grid, pre_r, pre_c, pre_small_cnt, pre_large_cnt):
        global ans
        pre_ind = rc2ind(pre_r, pre_c)
        pre_grid_list = tuple2list(pre_grid)
        if pre_ind == ind_end:
            ans += 1
            """
            print('---')
            for g in pre_grid:
                print(g)
            """
            return
        cur_ind = pre_ind + 1
        cur_r, cur_c = ind2rc(cur_ind)
        # 既に畳が敷いてある場合は、何もせず次に
        if pre_grid[pre_r][pre_c] != 0:
            dfs(pre_grid, cur_r, cur_c, pre_small_cnt, pre_large_cnt)

        # ここに、畳を敷くことを考える
        for i in range(1, 4):
            if i == 1:
                # 小さい畳を敷く
                if pre_small_cnt >= small_max:
                    continue
                cur_grid_list = tuple2list(pre_grid)
                cur_grid_list[pre_r][pre_c] = 1
                cur_grid = list2tuple(cur_grid_list)
                dfs(cur_grid, cur_r, cur_c, pre_small_cnt+1, pre_large_cnt)
            elif i == 2:
                # 大きい畳を縦に敷く
                if pre_large_cnt >= large_max:
                    continue
                if pre_r+1 >= r_end:
                    continue
                if pre_grid[pre_r+1][pre_c] != 0:
                    continue
                cur_grid_list = tuple2list(pre_grid)
                cur_grid_list[pre_r][pre_c] = 2
                cur_grid_list[pre_r+1][pre_c] = 2
                cur_grid = list2tuple(cur_grid_list)
                dfs(cur_grid, cur_r, cur_c, pre_small_cnt, pre_large_cnt+1)
            else:
                # 大きい畳を横に敷く
                if pre_large_cnt >= large_max:
                    continue
                if pre_c+1 >= c_end:
                    continue
                if pre_grid[pre_r][pre_c+1] != 0:
                    continue
                cur_grid_list = tuple2list(pre_grid)
                cur_grid_list[pre_r][pre_c] = 3
                cur_grid_list[pre_r][pre_c+1] = 3
                cur_grid = list2tuple(cur_grid_list)
                dfs(cur_grid, cur_r, cur_c, pre_small_cnt, pre_large_cnt+1)

    dfs(list2tuple(grid), 0, 0, 0, 0)
    print(ans)


def tuple2list(tup):
    ret = []
    for t in tup:
        ret.append(list(t))
    return ret


def list2tuple(lis):
    ret = []
    for li in lis:
        ret.append(tuple(li))
    ret = tuple(ret)
    return ret


main()
