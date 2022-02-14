# r, cに対し、横に敷く、縦に敷く、1マスのを敷く、しかないを全探索すると
# 4**4294967296とおり・・・間に合わない
ans = 0


def main():
    r_end, c_end, big_max, small_max = map(int, input().split())
    goal = (1 << (r_end*c_end))-1

    def dfs(pre_bit, small_used, big_used, pre_pos):
        # print(bin(pre_bit)[2:].zfill(r_end*c_end))
        if pre_bit == goal:
            global ans
            ans += 1
            return
        cur_pos = pre_pos + 1
        cur_r = cur_pos // c_end
        cur_c = cur_pos % c_end
        # cur_pos番目のbitに畳を敷く
        if pre_bit >> cur_pos & 1:
            # 1. 畳がすでに敷かれている場合は、次に行く
            dfs(pre_bit, small_used, big_used, cur_pos)
        else:
            # 2. 畳が敷かれていない場合は、1マスのを敷く
            if small_used + 1 <= small_max:
                cur_bit = pre_bit | (1 << cur_pos)
                dfs(cur_bit, small_used + 1, big_used, cur_pos)
            if big_used + 1 <= big_max:
                if cur_c + 1 < c_end:
                    # 3. 横に畳を敷く
                    if (pre_bit >> cur_pos + 1) & 1 == 0:
                        cur_bit = pre_bit | (1 << cur_pos) | (1 << (cur_pos + 1))
                        dfs(cur_bit, small_used, big_used + 1, cur_pos)
                if cur_r + 1 < r_end:
                    # 4. 縦に畳を敷く
                    if (pre_bit >> cur_pos + c_end) & 1 == 0:
                        cur_bit = pre_bit | (1 << cur_pos) | (1 << (cur_pos + c_end))
                        dfs(cur_bit, small_used, big_used + 1, cur_pos)

    dfs(0, 0, 0, -1)
    print(ans)


main()
